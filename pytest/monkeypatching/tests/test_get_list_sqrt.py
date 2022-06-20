import script_for_monkeypatching

def test_fake_sqrt(monkeypatch):
    def fake_sqrt(*args, **kwargs):
        return [1, 1, 1, 1]
        
    monkeypatch.setattr(script_for_monkeypatching, "sqrt", fake_sqrt)
    
    result_list = script_for_monkeypatching.get_list_sqrt([2, 4, 9])
    
    assert [1, 1, 1, 1] == result_list