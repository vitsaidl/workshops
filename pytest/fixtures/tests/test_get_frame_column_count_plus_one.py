import script_for_fixtures
import pandas as pd
import pytest

#by default fixture invoked once per function
#if we want to invoke it once per module @pytest.fixture(scope="module")
@pytest.fixture
def frame_for_test()->pd.DataFrame:
    return pd.DataFrame({"some_col":[1,2,3]})

def test_returned_expected_column_count_no_fixture():
    dummy_frame = pd.DataFrame({"some_col":[1,2,3]})
    
    expected_result = 2
    actual_result = script_for_fixtures.get_frame_column_count_plus_one(dummy_frame)
    
    assert expected_result == actual_result
    
def test_insert_called_once_no_fixture(mocker):
    dummy_frame = pd.DataFrame({"some_col":[1,2,3]})
    spy_insert = mocker.spy(pd.DataFrame, "insert")
    
    script_for_fixtures.get_frame_column_count_plus_one(dummy_frame)
    
    spy_insert.assert_called_once()
    
def test_returned_expected_column_count_used_fixture(frame_for_test):
    expected_result = 2
    actual_result = script_for_fixtures.get_frame_column_count_plus_one(frame_for_test)
    
    assert expected_result == actual_result
    
def test_insert_called_once_used_fixture(frame_for_test, mocker):

    spy_insert = mocker.spy(pd.DataFrame, "insert")
    
    script_for_fixtures.get_frame_column_count_plus_one(frame_for_test)
    
    spy_insert.assert_called_once()