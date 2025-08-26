from datetime import datetime
from typing import Any
from typing import Optional
from typing import Tuple

from sqlalchemy import Engine
from sqlalchemy import text


def update_log_running(
    cnxn: Engine,
    job: str,
    dttm_started: datetime,
    parent_id: Optional[int] = None,
) -> int:
    """
    Establish a run_id for the current run and insert a 'running' entry into
    the log table.

    Args:
        cnxn (Engine): SQLAlchemy Engine for the target database.
        job (str): Name of the current job.
        dttm_started (str): Job start timestamp in format YYYY-MM-DD HH:MM:SS.
        parent_id (int, optional): Run ID of the parent job, if applicable.

    Returns:
        int: Newly assigned run_id.
    """

    query_max_id = text("""
        SELECT MAX(run_id) AS run_id
          FROM [history]
    """)

    with cnxn.connect() as conn:
        result = conn.execute(query_max_id).scalar()
        run_id = (result or 0) + 1

        cols = [
            "run_id",
            "job",
            "dttm_started",
            "run_status",
        ]

        params: dict[str, Any] = {
            "run_id": run_id,
            "job": job,
            "dttm_started": dttm_started,
            "run_status": "running",
        }

        if parent_id is not None:
            cols.append("parent_id")
            params["parent_id"] = parent_id

        query_insert = text(
            f"""
            INSERT INTO [history] ({", ".join(cols)})
            VALUES ({", ".join([f":{col}" for col in cols])})
        """,
        )

        conn.execute(query_insert, params)
        conn.commit()

    return run_id


def update_log_finished(
    cnxn: Engine,
    run_id: int,
    dttm_started: datetime,
    run_status: str,
) -> Tuple[datetime, int]:
    """
    Record job completion details in the log table.

    Args:
        cnxn (Engine): SQLAlchemy Engine for the target database.
        run_id (int): Run ID for the current job run.
        dttm_started (str): Job start timestamp, format YYYY-MM-DD HH:MM:SS.
        run_status (str): Status of the job on completion.

    Returns:
        tuple[str, int]: finished timestamp as string, time taken in seconds.
    """

    dttm_finished = datetime.now()
    time_taken = int((dttm_finished - dttm_started).total_seconds())

    # Reduce the precision to match SQL Server
    dttm_finished_str = dttm_finished.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    query = text(
        f"""
        UPDATE [history]
           SET dttm_finished = '{dttm_finished_str}',
               time_taken = {time_taken},
               run_status = '{run_status}'
         WHERE run_id = {run_id}
    """,
    )

    with cnxn.connect() as conn:
        conn.execute(query)
        conn.commit()

    return dttm_finished, time_taken
