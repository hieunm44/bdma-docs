from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime
import os


with DAG(dag_id='process_web_log',
         start_date=datetime(2023, 11, 24),
         schedule_interval='@daily',
         description='A DAG for web log processing',
         tags=['mdsbw_asgmt4'],
         catchup=False):

#     task_1 = FileSensor(task_id='scan_for_log',
#                         filepath='../the_logs/log.txt')

    task_2 = BashOperator(task_id='extract_data',
                          bash_command="pwd > /opt/airflow/dags/the_log/log.txt",
                          env=os.environ
                        )

    # task_2 = BashOperator(task_id='extract_data',
    #                       bash_command="grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' 'the_logs/log.txt' > 'the_logs/extracted_data.txt'",
    #                       env=os.environ
    #                     )
    
    # task_3 = BashOperator(task_id='transform_data',
    #                       bash_command="grep '198.46.149.143' '../the_logs/extracted_data.txt' > '../the_logs/transformed_data.txt'")

    # task_4 = BashOperator(task_id='load_data',
    #                       bash_command="tar -czvf '../the_logs/weblog.tar' '../the_logs/transformed_data.txt'")

    # task_2
    # task_1 >> task_2 >> task_3 >> task_4