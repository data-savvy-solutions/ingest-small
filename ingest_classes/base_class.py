from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Generator

import pandas as pd
from cnxns import dbms as db
from sqlalchemy import text
# from datetime import datetime


class BaseClass(ABC):
    "Base class for Ingest"

    def __init__(
        self,
        cnxns: dict,
        schema: str,
    ) -> None:
        """
        Instantiate an instance of BaseClass.

        Instantiate an instance of BaseClass and define the class variables
        run_id, cnxns, and schema. Status is set to failed and error to an
        empty string by default.

        Args:
            run_id (Integer): ID of current run.
            cnxns (Dictionary): Dictionary of connections objects, expects a
                source and target key.
            schema (String): Schema for the output tables.

        Returns:
            None.
        """

        self.source = cnxns["source"]
        self.target = cnxns["target"]
        self.schema = schema
        self.status = "failed"
        self.error = ""

    @abstractmethod
    def read_data(
        self,
        entity_name: str,
        load_method: str,
        modified_field: str,
        max_modified: Any,
        chunksize: int,
    ) -> Generator:
        """
        Yields a Generator of DataFrames containing data from a source system.

        This function should be overwritten in each subclass.

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

        pass

    def read_params(
        self,
    ) -> dict:
        """
        Return a dictionary of entities.

        Read the entity_params table and return a dictionary with the entity as
        key, and a nested dictionary as value. The nested dictionary contains
        parameters about the table.

        Args:
            None.

        Returns:
            Dictionary: Dictionary of entities.
        """

        def _row_to_dict(row):
            return {
                row["table_name"]: {
                    "entity_name": row["entity_name"],
                    "business_key": row["business_key"],
                    "modified_field": row["modified_field"],
                    "load_method": row["load_method"],
                    "chunksize": row["chunksize"],
                },
            }

        df = db.dbms_reader(
            self.target,
            table_name="entity_params",
            schema=self.schema,
        )

        params = df.apply(
            lambda row: _row_to_dict(row),
            axis=1,
        ).tolist()

        return {
            key: value
            for parameter in params
            for key, value in parameter.items()
        }

    def read_history(
        self,
        table_name: str,
        modified_field: str,
    ) -> Any | None:
        """
        Returns a maximum modified value.

        Given a table name and a modified field, returns the maximum value
        from the instances history table for that table. The datatype of the
        returned value will be dependent on the subclass it's called from.

        Args:
            table_name: The name of the table.
            modified_field: The name of the field containing the modified
                value.

        Returns:
            Any | None: The maximum modified value.
        """

        query = f"""
            SELECT TOP(1) {modified_field}
              FROM {self.schema}.history
             ORDER BY run_id desc;
        """

        df = db.dbms_reader(
            self.target,
            query=text(query),
        )

        if df.empty:
            return None
        else:
            return df[modified_field]

    def __call__(
        self,
        cls_id: int,
    ) -> None:
        """
        Calls the functions of the class.

        Uses the details provided during instantiation, run each of the
        functions specified in the class.

        Args:
            cls_id (Integer): The run_id for the class instance.

        Returns:
            None.
        """

        params = self.read_params()

        for table, parameters in params.items():
            # start_time = datetime.now()
            # rows_processed = 0
            # chunk_count = 0

            # Set a default chunksize if none given
            chunksize_param = int(
                1000000 if pd.isna(parameters["chunksize"])
                else parameters["chunksize"],
            )

            max_modified = self.read_history(
                table,
                parameters["modified_field"],
            )

            for chunk in self.read_data(
                parameters["entity_name"],
                parameters["load_method"],
                parameters["modified_field"],
                max_modified,
                chunksize_param,
            ):
                print(chunk)
