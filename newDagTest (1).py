from codPython.coletaDados_2 import main
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import boto3
import toml
import random


def coleta_dados():
    main()
    
    
with DAG('dados_twitter',
          start_date= datetime(2022,11,4),
          schedule_interval= '30 * * * *',
          catchup=False) as dag:


    coleta_dados = PythonOperator(
        task_id='coleta_dados',
        python_callable= coleta_dados
    )

    valido = BashOperator(
        task_id='CargaCompleta',
        bash_command="echo 'StatusOK'"
    )


    coleta_dados >> valido
    
