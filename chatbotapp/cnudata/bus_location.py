from chatbotapp.info import bus_station_info as info
from datetime import *


def a1_1_departure_times():
    station_times = info.get_aline_times(8, 30, 00)
    return station_times


print(a1_1_departure_times())


def a1_2_departure_times():
    station_times = info.get_aline_times(8, 31, 00)
    return station_times


# print(a1_2_departure_times()[0])
#
# a = {}
# a["정심화"] = a1_1_departure_times()
# # print(a["정심화"][0] < datetime(year=2021, month=3, day=2, hour=8, minute=31))
# print(a["정심화"])
