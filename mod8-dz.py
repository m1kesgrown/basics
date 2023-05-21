from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_date = today - timedelta(days=today.weekday())
    end_date = start_date + timedelta(days=6)
    result = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for user in users:
        name = user['name']
        birthd = user['birthday'].date()

        if start_date <= birthd <= end_date or birthd < start_date:
            bd = birthd.weekday()
            if bd >= 5:
                bd = 0
            result[bd].append(name)

    for day in range(7):
        date = start_date + timedelta(days=day)
        weekday = date.strftime('%A')
        names = ', '.join(result[day])
        print(f"{weekday}: {names}")


users = [
    {'name': 'Yura', 'birthday': datetime(1990, 5, 15)},
    {'name': 'Marina', 'birthday': datetime(1985, 10, 3)},
    {'name': 'Volodimir', 'birthday': datetime(1992, 8, 20)},
    {'name': 'Anna', 'birthday': datetime(1998, 2, 12)},
    {'name': 'Yan', 'birthday': datetime(1995, 5, 17)},
    {'name': 'Alex', 'birthday': datetime(1997, 10, 5)},
    {'name': 'Olga', 'birthday': datetime(1993, 5, 20)},
    {'name': 'Daria', 'birthday': datetime(1991, 8, 18)},
]

get_birthdays_per_week(users)
