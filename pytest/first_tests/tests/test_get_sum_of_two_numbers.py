import math_script

def test_expected_sum_returned():
    first_number = 10
    second_number = 32
    expected_result = 42
    actual_result = math_script.get_sum_of_two_numbers(first_number, second_number)
    assert expected_result == actual_result