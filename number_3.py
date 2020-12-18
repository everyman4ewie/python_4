# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

# 1 вариант
print(f'{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# 2 вариант
# import random
# new_list = [random.randint(20, 240)]
# my_list = [new_list for new_list in range(220) if new_list % 20 == 0 or new_list % 21 ==0]
# print(my_list[1:])