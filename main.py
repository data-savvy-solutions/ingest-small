import yaml

from helpers.cnxns_helper import get_cnxns


def run(
    config: dict,
    *instances: str,
) -> None:

    cnxns = get_cnxns(config, *instances)
    print(cnxns.keys())


if __name__ == "__main__":

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    instances = "adventureworks"

    run(config, instances)
