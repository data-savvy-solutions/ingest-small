def get_ddl() -> dict:
    """
    Returns a dictionary of data types.

    Returns a dictionary of dictionaries. Each nested dictionary represents a
    table, with the key representing a column header and the value a data type.

    Args:
        None

    Returns:
        Dictionary: a dictionary of dictionaries representing tables and their
            data types.
    """

    schema = "ods_adventureworks"

    definitions = {}

    # labelling scripts allows multiple deploys
    definitions[f"{schema}_schema"] = f"""
        CREATE SCHEMA {schema};
    """

    definitions[f"{schema}_history"] = f"""
        CREATE TABLE [{schema}].[history](
               [id] [bigint] NOT NULL IDENTITY(1,1) PRIMARY KEY
               ,[run_id] [bigint] NOT NULL
               ,[table_name] [nvarchar](100) NOT NULL
               ,[start_time] [datetime] NOT NULL
               ,[end_time] [datetime] NOT NULL
               ,[time_taken] [int] NOT NULL
               ,[rows_processed] [int] NOT NULL
               ,[modifieddate] [datetime] NULL
    );"""

    # drop and create entity params to ensure latest data
    definitions[f"{schema}_drop_entity_parameters"] = f"""
        IF OBJECT_ID('{schema}.entity_params', 'U') IS NOT NULL
        DROP TABLE {schema}.entity_params
    ;"""

    definitions[f"{schema}_entity_params"] = f"""
        CREATE TABLE [{schema}].[entity_params](
               [table_name] [NVARCHAR](75) NOT NULL PRIMARY KEY
               ,[entity_name] [NVARCHAR](75) NOT NULL
               ,[business_key] [NVARCHAR](75) NOT NULL
               ,[modified_field] [NVARCHAR](75) NULL
               ,[load_method] [NVARCHAR](75) NOT NULL
               ,[chunksize] [INT] NULL
               ,[active] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_Department"] = f"""
        CREATE TABLE [{schema}].[Department](
            [DepartmentID] [SMALLINT] NOT NULL
            ,[Name] [VARCHAR](256) NOT NULL
            ,[GroupName] [VARCHAR](256) NOT NULL
            ,[ModifiedDate] [DATETIME] NOT NULL,
        );"""

    return definitions
