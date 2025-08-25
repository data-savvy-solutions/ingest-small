def populate_entity_list() -> dict:
    """
    Return a dictionary of INSERT SQL statement.

    Return a dictionary of INSERT SQL statement for the entity_parameters
    table.

    Args:
        None

    Returns:
        Dictionary: a dictionary of INSERT SQL statements.
    """

    entity_params = {
        "adventureworks": """
            INSERT INTO [ods_adventureworks].[entity_params] (
                table_name
                ,entity_name
                ,business_key
                ,modified_field
                ,ingest_method
                ,active
            )

            VALUES (
                'Department'
                ,'HumanResources.Department'
                ,'DepartmentID'
                ,'ModifiedDate'
                ,'incremental'
                ,1
            )

        ;""",
    }

    return entity_params
