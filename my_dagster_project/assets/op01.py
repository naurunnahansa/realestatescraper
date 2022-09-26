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
    print("asdas")

@op
def get_file_sizes():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for f in files:
        get_dagster_logger().info(f"Size of {f} is {os.path.getsize(f)}")

@job
def file_sizes_job():
    get_file_sizes()

if __name__ == "__main__":
    print("Runnnn!")
    materialize([my_op,my_opp])
    result = file_sizes_job.execute_in_process()
    print(result)
