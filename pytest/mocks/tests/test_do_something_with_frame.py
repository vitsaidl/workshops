import script_for_mocks
from unittest.mock import Mock

def test_insert_called_two_times():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame(mocked_object)
    expected_insert_calls = 2
    actual_insert_calls = mocked_object.insert.call_count
    
    assert expected_insert_calls == actual_insert_calls

def test_insert_called_once():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame(mocked_object)
    
    mocked_object.insert.assert_called_once()
    
def test_insert_called():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame(mocked_object)
    
    mocked_object.insert.assert_called()
    
def test_drop_called():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame(mocked_object)
    
    mocked_object.drop.assert_called()

def test_insert_called_last_time_with_expected_params():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame(mocked_object)
    expected_params = (1, "another_column", 142)
    #because call_args is a call object which have tuple at index 0
    actual_params = mocked_object.insert.call_args[0]
    assert expected_params == actual_params
    
def test_insert_called_both_times_with_expected_params():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame(mocked_object)
    
    first_expected_params = (1, "some_column", 42)
    second_expected_params = (1, "another_column", 142)

    first_call_params, second_call_params = mocked_object.insert.call_args_list
    first_actual_params = first_call_params[0]
    second_actual_params = second_call_params[0]
    assert first_expected_params == first_actual_params
    assert second_expected_params == second_actual_params
    


    