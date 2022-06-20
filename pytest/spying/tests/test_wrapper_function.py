import script_for_spying

def test_inner_function_called_with_expected_params(mocker):
    spy_get_nothing = mocker.spy(script_for_spying, "get_nothing")
    
    script_for_spying.wrapper_function()
    
    #don't do assert spy_something.assert_called_with(something)!
    spy_get_nothing.assert_called_with(42, "hello")