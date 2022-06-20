import freezegun
import datetime
import script_for_freezegun

def test_raw_use_freezer():
    expected_result = datetime.date(2022, 1, 21)
    
    freezer = freezegun.freeze_time("2022-01-28 12:00:01")
    freezer.start()
    actual_result = script_for_freezegun.get_date_week_ago()
    freezer.stop()
    
    assert expected_result == actual_result
    
def test_freezer_context_manager():
    expected_result = datetime.date(2022, 1, 21)
    
    with freezegun.freeze_time("2022-01-28 12:00:01"):
        actual_result = script_for_freezegun.get_date_week_ago()
    
    assert expected_result == actual_result

@freezegun.freeze_time("2022-01-28 12:00:01")
def test_freezer_decorator():
    expected_result = datetime.date(2022, 1, 21)
    
    actual_result = script_for_freezegun.get_date_week_ago()
    
    assert expected_result == actual_result