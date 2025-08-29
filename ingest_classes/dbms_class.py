from typing import Any
from typing import Generator

from cnxns import dbms as db
from sqlalchemy import text

from ingest_classes.base_class import BaseClass


class DBMSClass(BaseClass):
    "Class for ingestesting data from a DBMS system, extends BaseClass"

    def read_data(
        self,
        entity_name: str,
        load_method: str,
        modified_field: str,
        max_modified: Any,
        chunksize: int,
    ) -> Generator:
        """
        Yields a Generator of DataFrames containing data from a DBMS system.

        Reads data in from a DBMS table in chunks and yields a Generator of
        DataFrames.

        Args:
            entity_name (String): The entity to read data from.
            load_method (String): How to load the data, incrementally or
                truncate and populate.
            modified_field (String): The field representing when the record
                was last modified.
            chunksize (Integer): The size of each chunk of data to read-in.

        Returns
            Generator: A Generator of DataFrames container data from a source
                system.
        """

        query = f"""
            SELECT *
              FROM {entity_name}
        """

        if max_modified:
            # Convert precision to match SQL
            max_modified_str = (
                max_modified.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            )

            query += f"""
                WHERE {modified_field} > '{max_modified_str}'
                ORDER BY {modified_field} asc;
            """

        for chunk in db.dbms_read_chunks(
            self.source,
            query=text(query),
            chunksize=chunksize,
        ):
            yield chunk
