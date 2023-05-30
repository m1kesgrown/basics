from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    current_date = datetime.now()
    start_date = current_date - timedelta(days=current_date.weekday())
    end_date = start_date + timedelta(days=11)
    result = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],
              6: [], 7: [], 8: [], 9: [], 10: [], 11: []}

    for user in users:
        name = user['name']
        birthday_date = user['birthday']
        birthday_date = birthday_date.replace(year=current_date.year)
        delta_days = birthday_date - current_date

        if delta_days.days >= -1 and delta_days.days <= 12:
            birthday_day = birthday_date.weekday()
            if birthday_day == 5 or birthday_day == 6:
                birthday_day = 7
                result[birthday_day].append(name)
            else:
                result[birthday_day].append(name)

    for day in range(12):
        date = start_date + timedelta(days=day)
        weekday = date.strftime('%A')
        names = ','.join(result[day])

        print(f'{weekday}: {names}')


users = [
    {'name': 'Yura', 'birthday': datetime(1990, 6, 1)},
    {'name': 'Marina', 'birthday': datetime(1985, 5, 29)},
    {'name': 'Volodimir', 'birthday': datetime(1992, 6, 3)},
    {'name': 'Anna', 'birthday': datetime(1998, 2, 12)},
    {'name': 'Yan', 'birthday': datetime(1995, 6, 2)},
    {'name': 'Alex', 'birthday': datetime(1997, 10, 5)},
    {'name': 'Olga', 'birthday': datetime(1993, 5, 31)},
    {'name': 'Daria', 'birthday': datetime(1991, 6, 4)},
]

get_birthdays_per_week(users)
