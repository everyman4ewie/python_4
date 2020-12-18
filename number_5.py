# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import random
from functools import reduce
# 1 способо
def add(el1, el2):
    return el1 + el2

my_list = [random.randint(100, 1000) for _ in range(99, 1001)]
print(sorted(my_list, key=lambda i: i % 2))  # сортирую элементы на четные и нечетные и выбираю только четные
print(reduce(add, my_list))

# 2 способ (не совсем так работает...)
# new_list = []
# my_list = [random.randint(100, 1000) for _ in range(99, 1001)]
# new_list.append(my_list)
# new_list = [el for el in my_list if not el % 2]
# print(my_list)
# print(sum(my_list))