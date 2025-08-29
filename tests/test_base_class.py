import sys
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

# Ensure project root is on sys.path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))
from ingest_classes.base_class import BaseClass  # noqa: E402


# Minimal dummy subclass to satisfy abstract methods
class BaseClassDummy(BaseClass):
    def read_data(
        self,
        entity_name,
        load_method,
        modified_field,
        max_modified,
        chunksize,
    ):
        # Dummy generator implementation for testing
        yield pd.DataFrame()


@pytest.fixture
def base_class_instance():
    "Fixture to create a BaseClassDummy instance with dummy connections"

    cnxns = {
        "source": "dummy_source",
        "target": "dummy_target",
    }

    return BaseClassDummy(
        cnxns=cnxns,
        schema="test_schema",
    )


class TestBaseClass:
    """Unit tests for BaseClass methods."""

    def test_read_params(
        self,
        base_class_instance,
    ):
        "Test read_params returns the correct dictionary from a test DataFrame"

        test_data = pd.DataFrame([
            {
                "table_name": "customers",
                "entity_name": "Customer",
                "business_key": "customer_id",
                "modified_field": "last_update",
                "load_method": "full",
                "chunksize": 1000,
            },

            {
                "table_name": "orders",
                "entity_name": "Order",
                "business_key": "order_id",
                "modified_field": "modified_at",
                "load_method": "incremental",
                "chunksize": 500,
            },
        ])

        with patch(
            "ingest_classes.base_class.db.dbms_reader",
            return_value=test_data,
        ) as mock_reader:

            result = base_class_instance.read_params()

            expected = {
                "customers": {
                    "entity_name": "Customer",
                    "business_key": "customer_id",
                    "modified_field": "last_update",
                    "load_method": "full",
                    "chunksize": 1000,
                },

                "orders": {
                    "entity_name": "Order",
                    "business_key": "order_id",
                    "modified_field": "modified_at",
                    "load_method": "incremental",
                    "chunksize": 500,
                },
            }

            assert result == expected
            mock_reader.assert_called_once()

    def test_read_history(
        self,
        base_class_instance,
    ):
        "Test read_history returns the correct maximum value or None"

        # Case 1: DataFrame has data
        test_df = pd.DataFrame(
            [
                {"last_update": "2025-08-29T12:00:00"},
            ],
        )

        with patch(
            "ingest_classes.base_class.db.dbms_reader",
            return_value=test_df,
        ) as mock_reader:

            result = base_class_instance.read_history(
                table_name="customers",
                modified_field="last_update",
            )

            assert result == "2025-08-29T12:00:00"
            mock_reader.assert_called_once()

        # Case 2: DataFrame is empty
        empty_df = pd.DataFrame(
            columns=["last_update"],
        )

        with patch(
            "ingest_classes.base_class.db.dbms_reader",
            return_value=empty_df,
        ) as mock_reader_empty:

            result_none = base_class_instance.read_history(
                table_name="customers",
                modified_field="last_update",
            )

            assert result_none is None
            mock_reader_empty.assert_called_once()
