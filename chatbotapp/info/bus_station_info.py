from datetime import date, datetime, timedelta


def get_departure_time(hour, minute, second):
    year = date.today().year
    month = date.today().month
    day = date.today().day
    departure_time = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    return departure_time


def get_aline_times(hour, minute, second):
    arriving_time = get_departure_time(hour, minute, second)
    station_times = [arriving_time]

    for i in range(7):
        arriving_time += timedelta(minutes=15)
        str_time = arriving_time
        station_times.append(str_time)

    arriving_time += timedelta(minutes=45)
    station_times.append(arriving_time)

    for i in range(2):
        arriving_time += timedelta(minutes=15)
        str_time = arriving_time
        station_times.append(str_time)

    arriving_time += timedelta(hours=1, minutes=30)
    station_times.append(arriving_time)

    for i in range(3):
        arriving_time += timedelta(minutes=15)
        station_times.append(arriving_time)

    arriving_time += timedelta(minutes=45)
    station_times.append(arriving_time)

    for i in range(12):
        arriving_time += timedelta(minutes=15)
        station_times.append(arriving_time)

    arriving_time += timedelta(minutes=25)
    station_times.append(arriving_time)

    return station_times


def get_bline_times(hour, minute):
    arriving_time = get_departure_time(hour, minute)
    station_times = [arriving_time]

    for i in range(11):
        arriving_time += timedelta(minutes=10)
        str_time = arriving_time
        station_times.append(str_time)

    arriving_time += timedelta(minutes=40)
    station_times.append(arriving_time)

    for i in range(3):
        arriving_time += timedelta(minutes=10)
        str_time = arriving_time
        station_times.append(str_time)

    arriving_time += timedelta(minutes=20)
    station_times.append(arriving_time)

    arriving_time += timedelta(hours=1)

    for i in range(6):
        arriving_time += timedelta(minutes=10)
        station_times.append(arriving_time)

    arriving_time += timedelta(minutes=40)
    station_times.append(arriving_time)

    for i in range(19):
        arriving_time += timedelta(minutes=10)
        station_times.append(arriving_time)

    arriving_time += timedelta(minutes=15)
    station_times.append(arriving_time)

    return station_times

# print(len(get_bline_times(8, 30)))