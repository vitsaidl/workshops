import pandas as pd


def get_another_frame()->None:
    some_frame = pd.DataFrame({
        "first_col": [1, 2, 3],
        "second_col": [10, 20, 30]
    })
    
    some_frame.insert(1, "third_col", [40, 50, 60])
    some_frame.insert(1, "fourth_col", [400, 500, 600])
    frame_from_method = some_frame.copy()

    return frame_from_method 

def get_nothing(number:int, text:str)->None:
    return None

def wrapper_function()->None:
    get_nothing(42, "hello")

