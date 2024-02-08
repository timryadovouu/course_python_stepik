import math
from datetime import date, time, datetime, timedelta
import time
import calendar
from functools import reduce
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# alarm = time(7, 30, 25)
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))
#
# birthday = date(1992, 10, 6)
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


# try:
#     day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ: ').split('.')
#     my_date = date(int(year), int(month), int(day))
#     print(my_date)
# except ValueError:
#     print('Ошибка ввода')


# my_list = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
# print(*[item.strftime(f"%d/%m/%Y") for item in my_list], sep="\n")


# def print_good_dates(dates):
#     my_list = sorted(list(filter(lambda item: item.year == 1992 and (item.day + item.month) == 29, dates)))
#     if my_list:
#         print(*[item.strftime('%B %d, %Y') for item in my_list], sep='\n')


# def is_correct(day, month, year):
#     try:
#         date(year, month, day)
#         return True
#     except:
#         return False
#
# counter = 0
# date_q = input()
# while date_q != "end":
#     if is_correct(*map(int, date_q.split("."))):
#         print("Корректная")
#         counter += 1
#     else:
#         print("Некорректная")
#     date_q = input()
#
# print(counter)


# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
# def dts(dates):
#     times_of_purchases_am = list(filter(lambda dt: dt.hour < 12, times_of_purchases))
#     times_of_purchases_pm = list(filter(lambda dt: dt.hour > 12, times_of_purchases))
#     if len(times_of_purchases_am > times_of_purchases_pm): return "До полудня"
#     return "После полудня"
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
# date_time = sorted([datetime.combine(dates[i], times[i]) for i in range(len(dates))], key=lambda dt: dt.second)


# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# my_list = [(datetime.strptime(data[key][1], '%d.%m.%Y %H:%M:%S').timestamp() -
#            datetime.strptime(data[key][0], '%d.%m.%Y %H:%M:%S').timestamp()) for key in data.keys()]
# ind = my_list.index(min(my_list))
# minimum = (datetime.strptime(data["Дима"][1], '%d.%m.%Y %H:%M:%S').timestamp() -
#            datetime.strptime(data["Дима"][0], '%d.%m.%Y %H:%M:%S').timestamp())
# k = ""
# for key in data.keys():
#     m = (datetime.strptime(data[key][1], '%d.%m.%Y %H:%M:%S').timestamp() -
#            datetime.strptime(data[key][0], '%d.%m.%Y %H:%M:%S').timestamp())
#     if m < minimum:
#         minimum = m
#         k = key

# my_dict = {}
# with open('diary.txt', encoding='utf-8') as diary:
#     my_list= list(map(lambda line: line.strip().split(), diary.readlines()))   #чтение файла
#     dates = [datetime.strptime("".join(my_list[0]), '%d.%m.%Y;%H:%M')]   #m
#     x = []
#     m_index = [0]
#     ind = my_list.index([])
#     # my_dict.setdefault(datetime.strptime("".join(my_list[0]), '%d.%m.%Y;%H:%M'))   #первый ключ
#     # my_dict[datetime.strptime("".join(my_list[0]), '%d.%m.%Y;%H:%M')] = my_list[1:ind] # первое значение ключа
#     start, end = 0, 0
#     for i in range(0, len(my_list)):
#         if my_list[i] == []:
#             dates.append(datetime.strptime("".join(my_list[start]), '%d.%m.%Y;%H:%M'))   #список дат
#             my_dict.setdefault(datetime.strptime("".join(my_list[start]), '%d.%m.%Y;%H:%M'))   #словарь дат без значений
#             end = i
#             m_index.append(i)
#             my_dict[datetime.strptime("".join(my_list[start]), '%d.%m.%Y;%H:%M')] = my_list[start+1:end]
#             # x.append(my_list[start:end])
#             start = i+1
# m_index.append(len(my_list))
# my_dict.setdefault(datetime.strptime("".join(my_list[m_index[-2]+1]), '%d.%m.%Y;%H:%M'))
# my_dict[datetime.strptime("".join(my_list[m_index[-2]+1]), '%d.%m.%Y;%H:%M')] = my_list[m_index[-2]+2:m_index[-1]]
#
# print(m_index)       #29
# print(len(my_dict))
# for key, value in sorted(my_dict.items()):
#     print(key.strftime("%d.%m.%Y; %H:%M"))
#     for item in my_dict[key]:
#         print(*item)
#     print()

# def is_available_date(booked_dates, date_for_booking):  #86400
#     n_booked_dates = []
#     n_date_for_booking = []
#     for dt in booked_dates:
#         if "-" in dt:
#             ind = dt.index("-")
#             for _ in range(datetime.strptime(dt[0:ind], "%d.%m.%Y").toordinal(), datetime.strptime(dt[ind+1:], "%d.%m.%Y").toordinal()+1):
#                 n_booked_dates.append(_)
#         else:
#             n_booked_dates.append(datetime.strptime(dt, "%d.%m.%Y").toordinal())
#
#     if "-" in date_for_booking:
#         ind = date_for_booking.index("-")
#         for _ in range(datetime.strptime(date_for_booking[0:ind], "%d.%m.%Y").toordinal(),
#                        datetime.strptime(date_for_booking[ind + 1:], "%d.%m.%Y").toordinal() + 1):
#             n_date_for_booking.append(_)
#     else:

#         n_date_for_booking.append(datetime.strptime(date_for_booking, "%d.%m.%Y").toordinal())
#
#     return set(n_booked_dates).isdisjoint(set(n_date_for_booking))
#
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))

# my_list = [datetime.strptime(dt, "%d.%m.%Y") for dt in input().split()]
# answer = [abs((my_list[i] - my_list[i+1]).days) for i in range(len(my_list)-1)]

# def fill_up_missing_dates(dates):
#     delta =(max(map(lambda dt: datetime.strptime(dt, "%d.%m.%Y"), dates)) - min(map(lambda dt: datetime.strptime(dt, "%d.%m.%Y"), dates))).days
#     new_dates = [(min(map(lambda dt: datetime.strptime(dt, "%d.%m.%Y"), dates)) + timedelta(days=i)).strftime("%d.%m.%Y") for i in range(delta+1)]
#     return new_dates

# # start, end = datetime.strptime(input(), "%H:%M"), datetime.strptime(input(), "%H:%M")
# while (end - start).seconds/60 >= 45 and start < end:
#     print(f"{start.strftime('%H:%M')} - {(start + timedelta(minutes=45)).strftime('%H:%M')}")
#     start += timedelta(minutes=55)


data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
# upd = [(datetime.strptime(date_set[1], "%H:%M") - datetime.strptime(date_set[0], "%H:%M")).seconds//60 for date_set in data]
# upd_1 = reduce(lambda x, y: x+y, upd)

# my_dict = {_+1:0 for _ in range(7)}
# dt = datetime(year=1, month=1, day=1)
# while dt != datetime(year=9999, month=12, day=31):
#     if dt.day == 13:
#         my_dict[dt.isoweekday()] += 1
#     dt += timedelta(days=1)
# [print(my_dict[key]) for key in my_dict.keys()]

# timetable = {_+1:(time(hour=9),time(hour=21)) for _ in range(5)} | {_+6:(time(hour=10),time(hour=18)) for _ in range(2)}
# def shop_timetable(string):
#     m = string.split()
#     dt = datetime.strptime(m[0], "%d.%m.%Y").isoweekday()
#     our_timetable = timetable[dt]
#     tm = datetime.strptime(m[1], "%H:%M").time()
#     if our_timetable[0] <= tm <= our_timetable[1]:
#         tmdlt = (our_timetable[1].hour -  tm.hour)*60 - tm.minute                          # timedelta(hours=tm.hour, minutes=tm.minute)
#         return tmdlt
#     return "Магазин не работает"

# start, stop = datetime.strptime(input(), "%d.%m.%Y"), datetime.strptime(input(), "%d.%m.%Y")
# my_list = [start + timedelta(days=_) for _ in range((stop-start).days+2)]
# try:
#     new_start_date = min(list(filter(lambda dt: (dt.day + dt.month)%2 != 0 , my_list)))
#     # print(new_start_date, new_start_date.strftime("%A"))
#     # and dt.strftime("%A") != "Monday" and  dt.strftime("%A") != "Thursday"
#     while new_start_date <= stop:
#         if new_start_date.strftime("%A") != "понедельник" and  new_start_date.strftime("%A") != "четверг":
#             print(new_start_date.strftime("%d.%m.%Y -- %A"))
#         new_start_date += timedelta(days=3)
# except:
#     print()
# print(datetime.strptime("08.11.2021", "%d.%m.%Y").strftime("%A"))

#молодой сотрудник из ближайшей даты
# dt, members, counter = datetime.strptime(input(), "%d.%m.%Y"), [input().split() for _ in range(int(input()))], 0
# answ = [(abs(dt.month + dt.day -datetime.strptime(members[_][2], "%d.%m.%Y").month - datetime.strptime(members[_][2], "%d.%m.%Y").day))
#         for _ in range(len(members))]
# w = [min(abs((dt-datetime.strptime(members[_][2], "%d.%m.%Y").replace(year=dt.year)).days),
#          abs((dt-datetime.strptime(members[_][2], "%d.%m.%Y").replace(year=dt.year+1)).days))
#      for _ in range(len(members))]
# w_1 = [(dt-datetime.strptime(members[_][2], "%d.%m.%Y")).days for _ in range(len(members))]
# minimum, ind = 100_000, 0
# for i in range(len(w)):
#     if w[i] in range(1,8):
#         if w_1[i] <= minimum:
#             minimum = w_1[i]
#             ind = i
# if minimum == 100_000: print("Дни рождения не планируются")
# else: print(*members[ind][0:2])

#fakenews

# release_date, input_data = datetime(2022, 11, 8, 12), datetime.strptime(input(), "%d.%m.%Y %H:%M")
# td = release_date - input_data
# days, hours, minutes = td.days, td.seconds // 3600, (td.seconds // 60) % 60
# d, h, m = ["дня", "дней", "день"], ["часа", "часов", "час"], ["минут", "минута", "минуты"]
# pre_d, pre_h, pre_m = "", "", ""
# if days%10 in range(2,5) and days%100 not in range(12, 20):
#     pre_d = d[0]
# elif days%10 in range(5,10) or days%100 in range(11, 20) or days%10 == 0:
#     pre_d = d[1]
# else:
#     pre_d = d[2]
# if hours%10 == 1 and hours%100 != 11:
#     pre_h = h[2]
# elif hours%10 in range(2,5) and hours%100 not in range(12, 20):
#     pre_h = h[0]
# else:
#     pre_h = h[1]
# if minutes%10 == 1:
#     pre_m = m[1]
# elif minutes%10 == 2:
#     pre_m = m[2]
# else:
#     pre_m = m[0]
# print(release_date, input_data, days, hours, minutes, sep="\n")
# print(release_date - input_data)
# if release_date <= input_data:
#     print("Курс уже вышел!")
# elif days > 0:
#     if hours > 0:
#         if minutes > 0:
#             print(f"До выхода курса осталось: {days} {pre_d} и {hours} {pre_h}")
#         else:
#             print(f"До выхода курса осталось: {days} {pre_d}")
#     else:
#         if minutes > 0:
#             print(f"До выхода курса осталось: {days} {pre_d}")
#         else:
#             print(f"До выхода курса осталось: {days} {pre_d}")
# else:
#     if hours > 0:
#         if minutes > 0:
#             print(f"До выхода курса осталось: {hours} {pre_h} и {minutes} {pre_m}")
#         else:
#             print(f"До выхода курса осталось: {hours} {pre_h}")
#     else:
#         if minutes > 0:
#             print(f"До выхода курса осталось: {minutes} {pre_m}")

#


# s1, s2, s3 = time.time(), time.monotonic(), time.perf_counter()
# for i in range(5):
#     print(i)
#     time.sleep(0.3)
# e1, e2, e3 = time.time(), time.monotonic(), time.perf_counter()
# q1, q2, q3 = e1 - s1, e2 - s2, e3 - s3
# print(q1, q2, q3, sep="::::")

def calculate_it(func, *args):
    start = time.monotonic()
    answer = func(*args)
    end = time.monotonic()
    return answer, end-start
def get_the_fastest_func(funcs, arg):
    a = []
    for f in funcs:
        start = time.monotonic()
        ans = f(arg)
        end = time.monotonic()
        a.append(end - start)
        return funcs.index(min(a))

for name in calendar.day_abbr:
    print(name.title())
#
#
# print(calendar.month(2023, 9))
# calendar.prmonth(2023, 9)
#
# [print(__import__("calendar").isleap(int(input()))) for _ in range(int(input()))]
#
# info = input().split()
# english_names = list(calendar.month_abbr)
# print(calendar.month(int(info[0]), english_names.index(info[1])))
#
# dt = input().split()
# print(__import__("calendar").monthrange(int(dt[0]), list(calendar.month_name).index(dt[1]))[1])

def get_days_in_month(year, month):
    return [date(year, month = list(calendar.month_name).index(month), day=_+1) for _ in range(calendar.monthrange(year, list(calendar.month_name).index(month))[1])]
# print(get_days_in_month(2021, "Декабрь"))

def get_all_mondays(year):   #вывод всех понедельников
    answer = []
    for ind_m in range(1, len(list(calendar.month_name))):
        for ind_d in range(calendar.monthrange(year, list(calendar.month_name).index(calendar.month_name[ind_m]))[1]):
            if calendar.day_name[calendar.weekday(year=year, month=ind_m, day=ind_d+1)] == "понедельник":
                answer.append(date(year, month=ind_m, day=ind_d+1))
    return answer

def free_entrance(year):
    f_entr = []
    for ind_m in range(1,13):
        thursday_counter = 0
        for ind_d in range(calendar.monthrange(year, list(calendar.month_name).index(calendar.month_name[ind_m]))[1]):
            if calendar.day_name[calendar.weekday(year=year, month=ind_m, day=ind_d + 1)] == "четверг":
                thursday_counter +=1
                if thursday_counter == 3:
                    f_entr.append(date(year, month=ind_m, day=ind_d+1))
    return f_entr

print(*[datetime.strftime(dt, "%d.%m.%Y") for dt in free_entrance(int(input()))], sep="\n")