# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import count, cycle

i = int(input('Введите число с которого начинается счет: '))
k = int(input('Введите сколько элементов будет выводиться: '))
for el in count(i):  # идем с i-того элемента
    if el > k:
        break
    print(el)

# 1 вариант
new_list = []
my_list = input('Введите числа через запятую ')
new_list.extend(list(map(int, my_list.split(','))))
number = 1
q = int(input('Введите сколько раз будут выводиться числа: '))
for num in cycle(new_list):
    if number > q:
        break
    print(num)
    number += 1

# 2 вариант
# my_list = [1, 2, 7, 8, 5, 6, 11, 14, 12]
# new_list = cycle(my_list)
# number = 1
# q = int(input('Введите сколько раз будут выводиться числа: '))
# for i in cycle(new_list):
#     if number > q:
#         break
#     print(i)
#     number += 1

# 3 вариант
# new_list = []
# my_list = input('Введите числа через пробел ')
# lenning = int(input('Введите сколько раз будем выводить элементы: '))
# new_list.extend(list(map(int, my_list.split())))
# listing = cycle(new_list)
# if len(new_list) < lenning:
#     for val in new_list:
#         print(val)