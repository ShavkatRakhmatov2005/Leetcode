import datetime
def find_next_friday_13(date_str):
    day, month, year = map(int, date_str.split('.'))
    while True:
        if day == 13 and datetime.datetime(year, month, day).weekday() == 4:
            return f"13.{month:02d}.{year}"
        day += 1
        if day > 31: 
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

user_input = input("Sana (kun.oy.yil ko'rinishida)ni kiriting: ")
next_friday_13 = find_next_friday_13(user_input)
print("Chiqish (kun.oy.yil ko'rinishida):", next_friday_13)
