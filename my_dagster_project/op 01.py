from dagster import op
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
