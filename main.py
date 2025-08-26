import argparse
import logging
from datetime import datetime

import yaml

import ingest_classes as classes
from helpers.cnxns_helper import get_cnxns
from helpers.log_helper import update_log_finished
from helpers.log_helper import update_log_running


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def run(
    config: dict,
    *instances: str,
) -> None:

    dttm_started = datetime.now()
    job = "ingest"
    run_status = "succeeded"
    log_path = config["parameters"]["log_path"]

    fh = logging.FileHandler(f"{log_path}{job}.log")
    LOGGER.addHandler(fh)

    # denote new instance
    LOGGER.info("---")

    cnxns = get_cnxns(config, *instances)

    run_id = update_log_running(
        cnxns["mdh"],
        job,
        dttm_started,
    )

    LOGGER.info(f"{job}/{run_id} started: {dttm_started}")

    try:

        assert instances, (
            "You must specify at least one instance",
        )

        cls_dict = classes.class_dict
        cls_instances = {}

        if "adventureworks" in instances:
            cls_instances["adventureworks"] = cls_dict["DBMSClass"](
                {
                    "source": cnxns["adventureworks"],
                    "target": cnxns["ods"],
                },
                config["ods"]["adventureworks"],
            )

        if len(cls_instances) == 0:
            raise KeyError("Please specify a valid instance")

        else:

            for cls in cls_instances.keys():

                try:
                    cls_started = datetime.now()
                    cls_id = update_log_running(
                        cnxns["mdh"],
                        f"{job}_{cls}",
                        cls_started,
                        parent_id=run_id,
                    )

                    LOGGER.info(f"{cls}/{cls_id} started: {cls_started}")

                    cls_instances[cls](cls_id)
                    cls_status = cls_instances[cls].status
                    LOGGER.info(f"{cls}/{cls_id}: {cls_status}")

                    if cls_status == "failed":
                        run_status = "failed"
                        cls_error = cls_instances[cls].error
                        LOGGER.error(
                            f"{cls}/{cls_id}: raised an error: {cls_error}",
                        )

                # Ensures that any error is recorded but allows failover to the
                # next instance.
                except Exception:
                    cls_status = "failed"
                    LOGGER.error(
                        f"{cls}/{cls_id}: raised an error:", exc_info=True,
                    )

                finally:
                    cls_finished, cls_time_taken = update_log_finished(
                        cnxns["mdh"],
                        cls_id,
                        cls_started,
                        cls_status,
                    )
                    LOGGER.info(f"{cls}/{cls_id} finished: {cls_finished}")
                    LOGGER.info(f"{cls}/{cls_id} time_taken: {cls_time_taken}")

    # Ensures a graceful fail
    except Exception:
        run_status = "failed"
        LOGGER.error(f"{job}/{run_id}: raised an error:", exc_info=True)

    finally:
        dttm_finished, time_taken = update_log_finished(
            cnxns["mdh"],
            run_id,
            dttm_started,
            run_status,
        )

    LOGGER.info(f"{job}/{run_id}: {run_status}")
    LOGGER.info(f"{job}/{run_id} finished: {dttm_finished}")
    LOGGER.info(f"{job}/{run_id} time_taken: {time_taken}")


if __name__ == "__main__":

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instances", type=str, nargs="*", default=[])

    args = parser.parse_args()
    instances = args.instances

    run(config, *instances)
