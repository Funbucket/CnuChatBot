from datetime import date, datetime, timedelta


def get_time(hour, minute, second):
    year = date.today().year
    month = date.today().month
    day = date.today().day
    time = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    return time
