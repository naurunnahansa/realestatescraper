from dagster import op, asset, materialize
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

if __name__ == "__main__":
    print("Runnnn!")
    materialize([my_op,my_opp])
    materialize([myApple])
    print(my_op())
