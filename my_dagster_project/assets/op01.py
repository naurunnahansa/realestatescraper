from dagster import op, asset, materialize
from typing import Tuple

@asset
def my_input_op(abc, xyz):
    pass

@asset
def my_op():
    return "hello"
    
@asset
def my_opp():
    return "opp"

if __name__ == "__main__":
    print("Runnnn!")
    materialize([my_input_op,my_op,my_opp])
    print(my_opp())
