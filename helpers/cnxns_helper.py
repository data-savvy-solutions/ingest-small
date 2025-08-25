from cnxns import dbms as db


def get_cnxns(
    config: dict,
    *instances: str,
) -> dict:
    """
    Returns a dictionary of SQLAlchemy Engine objects.

    Returns a dictionary of SQLAlchemy Engine objects derived from given
    config dictionary and list of instances.

    Args:
        config (Dictionary): Config parameters.
        *instances (String): Name of instance, for example "adventureworks".
            May be passed multiple times.

    Returns:
        Dictionary: A dictionary of SQLAlchemy Engine objects.
    """

    sql_driver = config["parameters"]["sql_driver"]

    cnxns = {}

    ods = config["ods"]
    mdh = config["mdh"]

    ods_db = ods["database"]  # noqa: F841
    mdh_db = mdh["database"]  # noqa: F841

    for source in ["mdh", "ods"]:
        cnxns[source] = db.dbms_cnxn(
            ods["type"],
            ods["server"],
            ods["uid"],
            ods["pwd"],
            port=ods["port"],
            driver=sql_driver,
            database=f"{source}_db",
            trust=ods["trust_cert"],
        )

    ignore_params = ["type", "uid", "pwd", "port", "database", "trust_cert"]

    dbms = config["dbms"]
    dbms_sources = [
        source for source in list(dbms.keys())
        if not any(param in source for param in ignore_params)
    ]

    for source in dbms_sources:
        cnxns[source] = db.dbms_cnxn(
            dbms[f"{source}_type"],
            dbms[source],
            dbms[f"{source}_uid"],
            dbms[f"{source}_pwd"],
            port=dbms[f"{source}_port"],
            driver=sql_driver,
            database=dbms[f"{source}_database"],
            trust=dbms[f"{source}_trust_cert"],
        )

    return cnxns
