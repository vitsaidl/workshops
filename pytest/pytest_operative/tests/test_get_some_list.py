import some_tested_script

def test_this_will_fail():
    expected_result =  ["three"]
    actual_result = some_tested_script.get_some_list()
    
    assert expected_result == actual_result
