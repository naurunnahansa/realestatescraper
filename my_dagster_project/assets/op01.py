import os
from dagster import op, asset, materialize, job,get_dagster_logger
from typing import Tuple

@asset
def my_op():
    return "hello"

@asset
def my_opp():
    return "opp"

@op
def myApple():
    return "Apple"

@job
def file_sizes_job():
    myApple()

if __name__ == "__main__":
    print("Runnnn!")
    materialize([my_op,my_opp])
    result = file_sizes_job.execute_in_process()
