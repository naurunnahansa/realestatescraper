from dagster import op, asset, materialize
from typing import Tuple

@op
def my_input_op(abc, xyz):
    pass

@op
def my_op():
    return "hello"
    
@op
def my_opp():
    return "opp"

if __name__ == "__main__":
    materialize([my_input_op,my_op,my_opp])
