import script_for_monkeypatching
import pandas as pd

def test_something(monkeypatch):
    def fake_copy(*args, **kwargs):
        return pd.DataFrame({"fake_column": [42, 142]})
        
    monkeypatch.setattr(pd.DataFrame, "copy", fake_copy)
    
    result_frame = script_for_monkeypatching.get_some_frame()
    
    assert result_frame.columns == ["fake_column"]