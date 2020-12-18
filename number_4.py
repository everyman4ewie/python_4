# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

new_list = []
my_list = input('Введите числа через пробел ')
new_list.extend(list(map(int, my_list.split())))

# 1 вариант
new_my_list = [el for el in my_list if my_list.count(el) < 2]
new_my_list = [int(el) for el in new_my_list]
print(new_my_list)

# 2 вариант
# new_my_list = [int(el) for el in my_list if my_list.count(el) < 2]
# print(new_my_list)