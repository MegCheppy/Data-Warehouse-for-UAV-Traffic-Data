from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator


default_args{
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 4, 13),
    'retries': 0
}