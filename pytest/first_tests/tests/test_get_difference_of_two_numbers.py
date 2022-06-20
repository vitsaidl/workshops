import math_script

def test_expected_difference_returned():
    first_number = 20
    second_number = 5
    expected_result = 15
    actual_result = math_script.get_difference_of_two_numbers(first_number, second_number)
    assert expected_result == actual_result

def test_this_fill_fail():
    assert 1 == 2