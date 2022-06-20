from unittest.mock import MagicMock
import script_for_context

def test_open_called_correctly(monkeypatch):
    object_from_context = MagicMock()
    
    def fake_open(*args, **kwargs):
        context_object = MagicMock()
        context_object.__enter__.return_value = object_from_context
        return context_object
    
    monkeypatch.setattr("builtins.open", fake_open)

    script_for_context.create_html_page()
    
    expected_html_string = "<b>Hello world</b>"
    
    assert 1 == object_from_context.write.call_count

    args, _ = object_from_context.write.call_args
    assert expected_html_string == args[0]