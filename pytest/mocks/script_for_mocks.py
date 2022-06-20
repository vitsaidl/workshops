import pandas as pd

def do_something_with_frame(orig_frame:pd.DataFrame)->None:
    orig_frame.insert(1, "some_column", 42)
    orig_frame.insert(1, "another_column", 142)
    
def do_something_with_frame_args_kwargs(orig_frame:pd.DataFrame)->None:
    orig_frame.insert(1, "some_column", value=42)
    orig_frame.insert(1, "another_column", value=142)

def get_frame_without_col(orig_frame:pd.DataFrame, col_name:str)->pd.DataFrame:
    something = orig_frame.drop(column=col_name)
    return something