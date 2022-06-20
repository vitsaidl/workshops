import pandas as pd
from numpy import sqrt

def get_some_frame():
    some_frame = pd.DataFrame({
        "first_col": [1, 2, 3],
        "second_col": [10, 20, 30]
    })
    
    frame_from_method = some_frame.copy()

    return frame_from_method 

def get_list_sqrt(input_list):
    return sqrt(input_list)    