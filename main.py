''' Програма для визначення днів народження працівників '''
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    ''' Функція визнвчення днів народження на тиждньові '''
    date_today = date.today()
    weekend = date_today + timedelta(days=7)
    previos_day = date_today - timedelta(days=1)
    previos_2day = date_today - timedelta(days=2)
    dict_birthday = {}

    # Перевірка чи пустий список
    if len(users) < 1:
        return {}

    # Проходимо циклом по списку працівників
    for user in users:

        # День нардження працівника
        birthday = user.get('birthday').replace(year=date_today.year)
        birthday_new_year = user.get('birthday').replace(year=date_today.year+1)

        # Імя працівника
        name_user = user.get('name')

        # День тиждня
        day_week = birthday.strftime('%A')

    # Перевіряємо чи на цьому тиждні є день народження в новому році
        if birthday_new_year < weekend:
            birthday = birthday_new_year

    # Певевіряємо якщо сьогодні Понеділок, чи були дні народження на вихідних
        if date_today.strftime('%A') == 'Monday':
            if birthday == previos_day or birthday == previos_2day:
                dict_birthday.update({'Monday': [name_user]})

    # Відкидаємо дні народження які вже пройшли
        if birthday < date_today:
            continue

    # Відкидаємо дні народження які в майбутньому
        if weekend < birthday:
            continue

    # Певевіряємо чи день народження не в Суботу та Неділю
        if day_week == 'Saturday' or day_week == 'Sunday':
            day_week = 'Monday'

    # Певевіряємо чи є в словнику запис
        if day_week not in dict_birthday:
            dict_birthday.update({day_week:[]})

    # Додаємо в словник дні народження
        dict_birthday[day_week].append(name_user)

    return dict_birthday


if __name__ == "__main__":
    users_1 = [{"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},]
    result = get_birthdays_per_week(users_1)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
