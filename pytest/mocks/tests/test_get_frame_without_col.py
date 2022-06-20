import script_for_mocks
from unittest.mock import Mock

def test_insert_in_mock_returns_something():
    mocked_object = Mock()
    mocked_object.drop.return_value = "there should be a frame"
    returned_value = script_for_mocks.get_frame_without_col(mocked_object, "some_col")
    
    assert returned_value == "there should be a frame"