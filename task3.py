import re

def normalize_phone(phone_number):
  """
  Нормалізує телефонний номер до стандартного формату.

  Args:
    phone_number: Рядок з телефонним номером у будь-якому форматі.

  Returns:
    Нормалізований телефонний номер у вигляді рядка (наприклад, '+380501234567').
  """
  # Видаляємо всі символи, крім цифр та плюса
  cleaned_number = re.sub(r'[^\d+]', '', phone_number)

  # Перевіряємо наявність міжнародного коду
  if cleaned_number.startswith('+'):
    return cleaned_number
  elif cleaned_number.startswith('380'):
    return '+' + cleaned_number
  elif cleaned_number.startswith('0'):
    return '+38' + cleaned_number[1:]
  else:
    return '+38' + cleaned_number

# Приклад використання:
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)