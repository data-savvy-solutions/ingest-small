import importlib.util
import sys
from glob import glob


def get_ddl() -> dict:
    """
    Return dictionary of CREATE TABLE SQL statements.

    Collect CREATE TABLE SQL statements from adventureworks/ subdirectory and
    return as a single dictionary.

    Args:
        None

    Returns:
        Dictionary: CREATE TABLE SQL statements related to housing.
    """

    schema = "ods_adventureworks"

    modules = glob("definitions/adventureworks/*.py")

    tables = {
        f"{schema}_database": f"""
            CREATE SCHEMA {schema};
        """,
    }

    for module in modules:
        spec = importlib.util.spec_from_file_location(module, module)
        if not spec or not spec.loader:
            raise ImportError("Cannot load module 'my_module'")
        ddl = importlib.util.module_from_spec(spec)
        sys.modules[module] = ddl
        spec.loader.exec_module(ddl)
        tables.update(ddl.get_ddl())

    return tables
