import pandas as pd
from typing import List, Dict

def get_slightly_increased_number(orig_number:int)->float:
    increment = 0.001
    return orig_number + increment
    
def get_some_list()->List[int]:
    return [1, 2, 3]

def get_some_dict()->Dict[str,int]:
    return {"key_1":10, "key_2":20}

def get_some_frame()->pd.DataFrame:
    return pd.DataFrame({
        "column_1": [10, 20, 30],
        "column_2": [100, 200, 300]
    })

    
class UselessZeroDivisionException(Exception):
    pass
    
def get_division_result(first_number:int, second_number:int)->float:
    if second_number == 0:
        raise UselessZeroDivisionException
    
    return first_number/second_number
    
    