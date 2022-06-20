import pandas as pd

def get_frame_column_count_plus_one(input_frame:pd.DataFrame)->int:
    input_frame.insert(1, "some_col_name", [10, 20, 30])
    return input_frame.shape[1]