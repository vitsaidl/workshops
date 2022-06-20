import moduleshow.scripts_text

def test_double_string_returned():
    orig_string = "abcd"
    expected_result = "abcdabcd"
    actual_result = moduleshow.scripts_text.get_double_string(orig_string)
    assert expected_result == actual_result