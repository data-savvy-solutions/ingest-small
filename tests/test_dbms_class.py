import sys
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

# Ensure project root is on sys.path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))
from ingest_classes.dbms_class import DBMSClass  # noqa: E402


@pytest.fixture
def dbms_instance():
    "Fixture to create a DBMSClass instance with dummy connections"

    cnxns = {
        "source": "dummy_source",
        "target": "dummy_target",
    }

    return DBMSClass(
        cnxns=cnxns,
        schema="test_schema",
    )


class TestDBMSClass:
    """Unit tests for DBMSClass methods."""

    @pytest.mark.parametrize(
        "entity_name, modified_field, max_modified, expected_snippets",
        [
            (
                "customers",
                "modified_at",
                None,
                [
                    "SELECT *",
                    "FROM customers",
                ],  # no WHERE clause expected
            ),
            (
                "orders",
                "last_update",
                datetime(2025, 8, 29, 15, 0, 0, 123456),
                [
                    "SELECT *",
                    "FROM orders",
                    "WHERE last_update > '2025-08-29 15:00:00.123'",
                    "ORDER BY last_update asc",
                ],
            ),
        ],
    )
    def test_read_data(
        self,
        dbms_instance,
        entity_name,
        modified_field,
        max_modified,
        expected_snippets,
    ):
        """
        Test read_data builds the correct SQL query under different conditions
        """

        test_chunk = MagicMock()
        with patch(
            "ingest_classes.dbms_class.db.dbms_read_chunks",
            return_value=[test_chunk],
        ) as mock_db:
            chunks = list(
                dbms_instance.read_data(
                    entity_name=entity_name,
                    load_method="incremental",
                    modified_field=modified_field,
                    max_modified=max_modified,
                    chunksize=100,
                ),
            )

        # Ensure generator yields the mocked chunk
        assert chunks == [test_chunk]

        # Inspect the query string passed to dbms_read_chunks
        called_query = mock_db.call_args[1]["query"].text
        for snippet in expected_snippets:
            assert snippet in called_query
