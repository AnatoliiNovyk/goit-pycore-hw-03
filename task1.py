from datetime import datetime, date

def get_days_from_today(date_str):
  """
  Розраховує кількість днів між заданою датою і поточною датою.

  Args:
    date_str: Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'.

  Returns:
    Ціле число, яке вказує на кількість днів від заданої дати до поточної.
    Повертає None, якщо формат дати неправильний.
  """
  try:
    given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    today = date.today()
    difference = today - given_date
    return difference.days
  except ValueError:
    return None

# Приклад використання:
date_to_check = "2021-10-09"
days_difference = get_days_from_today(date_to_check)

if days_difference is not None:
  print(f"Кількість днів між {date_to_check} та сьогоднішньою датою: {days_difference}")
else:
  print(f"Неправильний формат дати: {date_to_check}")

# Перевірка з прикладом з умови (сьогодні 5 травня 2021 року):
# Оскільки зараз 3 квітня 2025 року, результат буде іншим.
# Для перевірки прикладу, можна закоментувати попередній приклад
# та розкоментувати наступні рядки:
# from datetime import date
# today_example = date(2021, 5, 5)
# date_to_check_example = "2021-10-09"
# given_date_example = datetime.strptime(date_to_check_example, '%Y-%m-%d').date()
# difference_example = today_example - given_date_example
# print(f"Приклад: Кількість днів між {date_to_check_example} та 5 травня 2021 року: {difference_example.days}")

# Перевірка з датою в майбутньому:
future_date = "2025-05-10"
days_to_future = get_days_from_today(future_date)
if days_to_future is not None:
  print(f"Кількість днів між сьогоднішньою датою та {future_date}: {days_to_future}")
else:
  print(f"Неправильний формат дати: {future_date}")

# Перевірка з неправильним форматом дати:
wrong_format_date = "2025/04/03"
days_wrong_format = get_days_from_today(wrong_format_date)
if days_wrong_format is None:
  print(f"Тест з неправильним форматом дати '{wrong_format_date}': отримано None")
else:
  print(f"Тест з неправильним форматом дати '{wrong_format_date}': отримано {days_wrong_format}")
