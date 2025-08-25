import argparse
import importlib.util
import sys
from glob import glob

import sqlalchemy as sa
import yaml
from sqlalchemy import Engine
from sqlalchemy.exc import ProgrammingError

from helpers.cnxns_helper import get_cnxns


def _deploy_tables(
    cnxn: Engine,
    *instances: str
) -> None:
    """
    Execute CREATE TABLE SQL Scripts.

    Given a config object and a SQL ALCHEMY engine object, collect
    CREATE TABLE SQL Scripts from the definitions subdirectory and iterate
    over the resultant dictionary, exectuing the scripts against the engine.

    Args:
        ddl_dict (Dictionary): Dictionary of CREATE SQL Scripts.
        cnxn (Engine): SQL ALCHEMY engine object for database.
        *instances (String): One or more instances to run deploy for.

    Returns:
        None
    """

    modules = []
    exceptions = []
    for instance in instances:
        ddl = glob(f"definitions/{instance}.py")
        if len(ddl) > 0:
            modules.extend(glob(f"definitions/{instance}.py"))
        else:
            exceptions.append(instance)

        err = f"{', '.join(exceptions)} not valid instance(s) for deploy"
        assert len(exceptions) == 0, err

    data_definition_libraries = {}
    for module in modules:

        spec = importlib.util.spec_from_file_location(module, module)
        if not spec or not spec.loader:
            raise ImportError("Cannot load module 'my_module'")

        definitions = importlib.util.module_from_spec(spec)
        sys.modules[module] = definitions
        spec.loader.exec_module(definitions)
        data_definition_libraries.update(definitions.get_ddl())

    with cnxn.connect() as c:
        for ddl in data_definition_libraries.values():
            try:
                c.execute(sa.text(ddl))
            except ProgrammingError as e:
                error = repr(e)
                if "There is already an object named" in error:
                    pass  # the table already exists
                elif "already exists" in error:
                    pass  # the database already exists
                else:
                    raise Exception(error)
        c.close()


def run(
    config: dict,
    *instances: str,
) -> None:
    """
    Main run function.
    """

    cnxn = get_cnxns(config)["ods"]
    print(cnxn)

    _deploy_tables(cnxn, *instances)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instances", type=str, nargs="*", default=[])

    args = parser.parse_args()
    instances = args.instances

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    run(config, *instances)
