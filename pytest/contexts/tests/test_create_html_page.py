from unittest.mock import Mock, MagicMock
import script_for_context

def test_open_called_once(monkeypatch):
    fake_file_object = Mock()
    
    def fake_open(*args, **kwargs):
        context_object = MagicMock()
        context_object.__enter__.return_value = fake_file_object
        return context_object
    
    monkeypatch.setattr("builtins.open", fake_open)
    
    script_for_context.create_html_page()

    assert 1 == fake_file_object.write.call_count


def test_open_called_with_expected_argument(monkeypatch):
    fake_file_object = Mock()
    
    def fake_open(*args, **kwargs):
        context_object = MagicMock()
        context_object.__enter__.return_value = fake_file_object
        return context_object
    
    monkeypatch.setattr("builtins.open", fake_open)

    script_for_context.create_html_page()
    
    expected_html_string = "<b>Hello world</b>"

    args, _ = fake_file_object.write.call_args
    assert expected_html_string == args[0]