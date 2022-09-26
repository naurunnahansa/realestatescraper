from dagster import op
from typing import Tuple


@op(out={"int_output": Out(), "str_output": Out()})
def my_multiple_output_annotation_op() -> Tuple[int, str]:
    return (5, "foo")