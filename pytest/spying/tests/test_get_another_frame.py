import script_for_spying
import pandas as pd

def test_insert_called_twice_at_real(mocker):

    spy_insert = mocker.spy(pd.DataFrame, "insert")
    
    script_for_spying.get_another_frame()
    
    expected_call_count = 2
    actual_call_count = spy_insert.call_count
    
    assert expected_call_count == actual_call_count

def test_insert_called_twice_at_fake(monkeypatch, mocker):
    def fake_insert(*args, **kwargs):
        pass
    
    monkeypatch.setattr(pd.DataFrame, "insert", fake_insert)
    spy_insert = mocker.spy(pd.DataFrame, "insert")
    
    script_for_spying.get_another_frame()
    
    expected_call_count = 2
    actual_call_count = spy_insert.call_count
    
    assert expected_call_count == actual_call_count