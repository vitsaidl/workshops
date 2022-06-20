import script_for_mocks
from unittest.mock import Mock

def test_insert_called_last_time_with_expected_params():
    mocked_object = Mock()
    script_for_mocks.do_something_with_frame_args_kwargs(mocked_object)
    expected_args = (1, "another_column")
    expected_kwargs = {"value":142}
    
    actual_args = mocked_object.insert.call_args[0]
    actual_kwargs = mocked_object.insert.call_args[1]
    
    assert expected_args == actual_args
    assert expected_kwargs == actual_kwargs