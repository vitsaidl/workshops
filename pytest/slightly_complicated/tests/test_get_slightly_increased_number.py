import slightly_complicated
import pytest
import pandas as pd

def test_incrase_works():
    orig_number = 5
    expected_result = 5.001
    actual_result = slightly_complicated.get_slightly_increased_number(orig_number)
    
    assert actual_result == pytest.approx(expected_result, abs=0.0005)

def test_this_will_fail():
    orig_number = 5
    expected_result = 5.002
    actual_result = slightly_complicated.get_slightly_increased_number(orig_number)
    
    assert actual_result == pytest.approx(expected_result, abs=0.0005)

def test_increased_number_is_float():
    orig_number = 5
    actual_result = slightly_complicated.get_slightly_increased_number(orig_number)
    assert isinstance(actual_result, float)
    
def test_increased_number_is_integer():
    orig_number = 5
    actual_result = slightly_complicated.get_slightly_increased_number(orig_number)
    assert isinstance(actual_result, int)

def test_expected_list():
    expected_result = [1, 2, 3]
    actual_result = slightly_complicated.get_some_list()
    assert expected_result == actual_result

def test_expected_dict():
    expected_result = {"key_2":20, "key_1":10}
    actual_result = slightly_complicated.get_some_dict()
    assert expected_result == actual_result

def test_naive_expected_frame():
    expected_result = pd.DataFrame({
        "column_1": [10, 20, 30],
        "column_2": [100, 200, 300]
    })
    actual_result = slightly_complicated.get_some_frame()
    assert expected_result == actual_result

def test_expected_frame():
    expected_result = pd.DataFrame({
        "column_1": [10, 20, 30],
        "column_2": [100, 200, 300]
    })
    actual_result = slightly_complicated.get_some_frame()
    frames_differences = pd.testing.assert_frame_equal(expected_result, actual_result)
    assert frames_differences is None

def test_exception_raised():
    first_number = 10
    second_number = 0
    with pytest.raises(slightly_complicated.UselessZeroDivisionException):
        slightly_complicated.get_division_result(first_number, second_number)