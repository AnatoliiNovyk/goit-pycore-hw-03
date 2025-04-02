import random

def get_numbers_ticket(min_val, max_val, quantity):
  """
  Генерує набір унікальних випадкових чисел для лотерейних квитків.

  Args:
    min_val: Мінімальне можливе число у наборі (не менше 1).
    max_val: Максимальне можливе число у наборі (не більше 1000).
    quantity: Кількість чисел, які потрібно вибрати (значення між min та max).

  Returns:
    Відсортований список випадково вибраних унікальних чисел.
    Повертає пустий список, якщо параметри не відповідають обмеженням.
  """
  if not (1 <= min_val <= max_val <= 1000 and min_val <= quantity <= max_val):
    return []

  return sorted(random.sample(range(min_val, max_val + 1), quantity))

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

another_ticket = get_numbers_ticket(1, 36, 5)
print("Ще один квиток:", another_ticket)

invalid_ticket = get_numbers_ticket(1, 10, 15)
print("Недійсний квиток:", invalid_ticket)

invalid_range = get_numbers_ticket(1001, 1050, 5)
print("Недійсний діапазон:", invalid_range)

invalid_quantity = get_numbers_ticket(1, 50, 0)
print("Недійсний розмір:", invalid_quantity)