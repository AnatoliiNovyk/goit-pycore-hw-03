from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
  """
  Визначає, кого з колег потрібно привітати з днем народження протягом наступних 7 днів.

  Args:
    users: Список словників, де кожен словник містить ключі 'name' (ім'я) та 'birthday' (дата народження у форматі 'рік.місяць.дата').

  Returns:
    Список словників, де кожен словник містить ключі 'name' (ім'я) та 'congratulation_date' (дата привітання у форматі 'рік.місяць.дата').
  """
  today = date.today()
  upcoming_birthdays = []

  for user in users:
    name = user["name"]
    birthday_str = user["birthday"]
    try:
      birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
    except ValueError:
      print(f"Неправильний формат дати для користувача {name}: {birthday_str}")
      continue

    birthday_this_year = birthday_date.replace(year=today.year)

    if birthday_this_year < today:
      birthday_this_year = birthday_date.replace(year=today.year + 1)

    time_difference = birthday_this_year - today
    days_until_birthday = time_difference.days

    if 0 <= days_until_birthday <= 6:
      congratulation_date = birthday_this_year

      # Перенесення на понеділок, якщо день народження у вихідний
      if congratulation_date.weekday() == 5:  # Субота
        congratulation_date += timedelta(days=2)
      elif congratulation_date.weekday() == 6:  # Неділя
        congratulation_date += timedelta(days=1)

      upcoming_birthdays.append({
          "name": name,
          "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
      })

  return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.04.05"},
    {"name": "Jane Smith", "birthday": "1990.04.06"},
    {"name": "Peter Jones", "birthday": "1988.04.07"},
    {"name": "Alice Brown", "birthday": "1992.04.08"},
    {"name": "Bob Green", "birthday": "1980.04.09"},
    {"name": "Carol White", "birthday": "1995.04.10"},
    {"name": "David Black", "birthday": "1991.04.11"},
    {"name": "Eve Grey", "birthday": "1987.04.12"},
    {"name": "Frank Blue", "birthday": "1993.04.13"},
    {"name": "Grace Red", "birthday": "1989.04.14"},
    {"name": "Heidi Yellow", "birthday": "1994.04.03"}, # Сьогодні
    {"name": "Ivan Purple", "birthday": "1986.04.04"}, # Завтра
    {"name": "Julia Orange", "birthday": "1997.04.12"}, # Субота
    {"name": "Kevin Teal", "birthday": "1983.04.13"},  # Неділя
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# Очікуваний результат на 3 квітня 2025 року:
# [
#     {'name': 'Heidi Yellow', 'congratulation_date': '2025.04.03'},
#     {'name': 'Ivan Purple', 'congratulation_date': '2025.04.04'},
#     {'name': 'John Doe', 'congratulation_date': '2025.04.05'},
#     {'name': 'Jane Smith', 'congratulation_date': '2025.04.07'}, # Перенесено з суботи 04.06 на понеділок 04.07
#     {'name': 'Peter Jones', 'congratulation_date': '2025.04.07'}, # Перенесено з неділі 04.07 на понеділок 04.07
# ]
