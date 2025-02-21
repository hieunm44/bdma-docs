from pendulum import datetime, duration

# Airflow Operators are templates for tasks and encompass the logic that your DAG will actually execute.
# To use an operator in your DAG, you first have to import it.
# To learn more about operators, see: https://registry.astronomer.io/.

# DAG and task decorators for interfacing with the TaskFlow API
from airflow.decorators import dag, task, task_group

# A function that sets sequential dependencies between tasks including lists of tasks
from airflow.models.baseoperator import chain

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.weekday import BranchDayOfWeekOperator

# Used to label node edges in the Airflow UI
from airflow.utils.edgemodifier import Label

# Used to determine the day of the week
from airflow.utils.weekday import WeekDay


# When using the DAG decorator, the "dag" argument doesn't need to be specified for each task.
# The "dag_id" value defaults to the name of the function it is decorating if not explicitly set.
# In this example, the "dag_id" value would be "example_dag_advanced".
@dag(
    # This DAG is set to run for the first time on January 1, 2023.
    # Best practice is to use a static start_date.
    # Subsequent DAG runs are instantiated based on the "schedule" parameter below.
    start_date=datetime(2023, 1, 1),
    # This defines how many instantiations of this DAG (DAG Runs) can execute concurrently. In this case,
    # we're only allowing 1 DAG run at any given time, as opposed to allowing multiple overlapping DAG runs.
    max_active_runs=1,
    # This defines how often your DAG will run, or the schedule by which DAG runs are created. It can be
    # defined as a cron expression, custom timetable, existing presets or using the Dataset feature.
    # This DAG uses a preset to run daily.
    schedule="@daily",
    # Default settings applied to all tasks within the DAG; can be overwritten at the task level.
    default_args={
        "owner": "community",  # Defines the value of the "owner" column in the DAG view of the Airflow UI
        "retries": 2,  # If a task fails, it will retry 2 times.
        "retry_delay": duration(
            minutes=3
        ),  # A task that fails will wait 3 minutes to retry.
    },
    default_view="graph",  # This defines the default view for this DAG in the Airflow UI
    # When catchup=False, your DAG will only run for the latest schedule interval. In this case, this means
    # that tasks will not be run between January 1st, 2023 and 1 day ago. When turned on, this DAG's first run
    # will be for today, per the @daily schedule
    catchup=False,
    tags=["example"],  # If set, this tag is shown in the DAG view of the Airflow UI
)
def hieu():
    BashOperator(
        task_id='weekday_activities',
        # This is the Bash command to run
        bash_command=f"pwd > /opt/airflow/a.txt",
    )


hieu()
