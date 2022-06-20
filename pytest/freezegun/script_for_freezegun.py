import datetime

def get_date_week_ago():
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    return week_ago