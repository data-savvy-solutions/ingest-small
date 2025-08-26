from datetime import datetime

import yaml

from helpers.cnxns_helper import get_cnxns
from helpers.log_helper import update_log_finished
from helpers.log_helper import update_log_running


def run(
    config: dict,
    *instances: str,
) -> None:

    dttm_started = datetime.now()
    job = "ingest"
    run_status = "failed"

    cnxns = get_cnxns(config, *instances)

    run_id = update_log_running(
        cnxns["mdh"],
        job,
        dttm_started,
    )

    update_log_finished(
        cnxns["mdh"],
        run_id,
        dttm_started,
        run_status,
    )


if __name__ == "__main__":

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    instances = "adventureworks"

    run(config, instances)
