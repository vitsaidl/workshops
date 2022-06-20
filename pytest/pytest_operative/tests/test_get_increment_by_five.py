import some_tested_script
import pytest

def test_simple_example_1():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result

def test_simple_example_2():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result
    
def test_simple_exercise():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result

def test_trivial_exercise():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result

@pytest.mark.computation
def test_marked_as_computation():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result
    
@pytest.mark.something
def test_marked_as_something():
    orig_number = 1
    expected_result = 7
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result
    
@pytest.mark.computation
def test_marked_as_computation_too():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result

@pytest.mark.skip    
def test_to_skip():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result

@pytest.mark.xfail
def test_to_maybe_fail():
    orig_number = 1
    expected_result = 6
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result    
    
@pytest.mark.xfail
def test_to_fail():
    orig_number = 1
    expected_result = 7
    actual_result = some_tested_script.get_increment_by_five(orig_number)
    assert expected_result == actual_result

@pytest.mark.parametrize("some_input, expected_result", [(11, 16), (20, 25), (20, 26)])   
def test_parametrized(some_input, expected_result):
    actual_result = some_tested_script.get_increment_by_five(some_input)
    assert expected_result == actual_result