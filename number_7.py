from math import factorial
from itertools import count

# 1 вариант
def fact():
    n = int(input('С какого элемента будет считать факториал: '))
    for el in count(n):  # идем с n-ого элемента
        yield factorial(el)  # выдает значение факториала поэлементно

while True:
    try:
        generator = fact()
        num = 0
        degree = int(input('Введите сколько элементов будет считать факториал: '))
        if degree < 0:  # делаю проверку на ввод степени. Если отрицательная, то вылезает ошибка
            raise RecursionError  # ключ ошибки
    except RecursionError:
        print('Ошибка. Вы ввели отрицательное число!')
    else:
        for i in generator:
            if num < degree:  # пока начальный элемент не превысит
                print(i)
                num += 1
            else:
                break
        break


# 2 вариант
# def fact():
#     degree = int(input('Введите сколько элементов будет считать факториал: '))
#     print(factorial(degree))
#     return
#
# fact()


# 3 вариант
# def fact():
#     for el in count():  # идем с 1-ого элемента
#         yield factorial(el)
#
# while True:
#     try:
#         generator = fact()
#         num = 0
#         degree = int(input('Введите сколько элементов будет считать факториал: '))
#         if degree < 0:
#             raise RecursionError
#     except RecursionError:
#         print('Ошибка. Вы ввели отрицательное число!')
#     else:
#         for i in generator:
#             if num < degree:
#                 print(i)
#                 num += 1
#             else:
#                 break
#         break