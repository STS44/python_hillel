# Practice. Strings, lists, loops. List generators, sets.
from collections import defaultdict

# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# int_num = int(input("Enter integer number: "))
# int_to_str = str(int_num)
# zero = "0"
# result = int_to_str.count(zero)
# print(f"Number of zero in integer: {result}")

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# int_num = int(input("Enter integer number: "))
# count_zero = 0
# while int_num % 10 == 0:
#     int_num //= 10
#     count_zero += 1
# print(f"Number of zero in the end of integer: {count_zero}")

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

# my_list = ["qwe", "rty", "sel", "ect"]
# print(f"my list: {my_list}")
# new_list = list()
# for item in my_list:
#     if my_list.index(item) % 2 == 0:
#         item = item[::-1]
#     else:
#         item = item
#     new_list.append(item)
# print(f"new list: {new_list}")

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте в new_list. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1, 2, 3, 4]
# print(f"My list: {my_list}")
# my_list += [my_list.pop(0)]
# new_list = []
# for item in my_list:
#     new_list.append(item)
# print(f"New list: {new_list}")

# 5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4]
# print(f"My list: {my_list}")
# my_list += [my_list.pop(0)]
# print(f"My updated list: {my_list}")

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

# my_str = "43 больше чем 34 но меньше чем 56"
# print(f"My string: {my_str}")
# str_1 = my_str.split()
# sum = 0
# for item in str_1:
#     if item.isdigit():
#         sum += int(item)
# print(f"Sum of numbers: {sum}")

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

# my_str = "My long string"
# print(f"My string: {my_str}")
# l_limit = "o"
# r_limit = "g"
# result = my_str[my_str.find(l_limit)+1:my_str.rfind(r_limit)]
# print(f"Substring: {result}")

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

# my_str = "abcde"
# print(f"My string: {my_str}")
# my_list = [my_str[idx:idx+2] for idx in range(0, len(my_str), 2)]
# result = []
# for item in my_list:
#     if len(item) % 2 == 0:
#         item = item
#     else:
#         item = item + "_"
#     result.append(item)
# print(f"My result: {result}")

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# print(f"My list: {my_list}")
# counter = 0
# new_list = []
# for item in range(1, len(my_list)-1):
#     if my_list[item - 1] < my_list[item] > my_list[item + 1]:
#         counter += 1
# print(f"Number of items in list that exceed sum of their adjacent items: {counter}")

# 10. Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

# а) Определить возраст самого молодого человека и поместить в новый список имена всех людей,
# чей возраст совпадает с этим минимальным возрастом.

# dict_list = [{"name": "John", "age": 15}, {"name": "Jacob", "age": 25}, {"name": "Jessica", "age": 35}, {"name": "Jack", "age": 45}]
# print(f"list of dictionaries Persons: {dict_list}")
# age_list = []
# for key in dict_list:
#     age_list.append(key["age"])
#     min_age = min(age_list)
# name_min_age = []
# for item in dict_list:
#     if item["age"] == min_age:
#         name_min_age.append(item["name"])
# print(f"Name of the youngest person in list: {name_min_age}")

# б) Определить самое длинное имя и поместить в новый список имена всех людей,
# чье имя по длине совпадает с этой длиной.

# dict_list = [{"name": "John", "age": 15}, {"name": "Jacob", "age": 25}, {"name": "Jessica", "age": 35}, {"name": "Jack", "age": 45}]
# print(f"list of dictionaries Persons: {dict_list}")
# name_list = []
# for key in dict_list:
#     name_list.append(key["name"])
#     max_name = max(name_list, key=len)
# name_list_res = []
# for item in dict_list:
#     if len(item["name"]) == len(max_name):
#         name_list_res.append(item["name"])
# print(f"Names of persons whose name is as long as the longest in list: {name_list_res}")

# в) Посчитать среднее количество лет всех людей из списка.

# dict_list = [{"name": "John", "age": 15}, {"name": "Jacob", "age": 25}, {"name": "Jessica", "age": 35}, {"name": "Jack", "age": 45}]
# print(f"list of dictionaries Persons: {dict_list}")
# my_list = []
# for key in dict_list:
#     my_list.append(key["age"])
# result = sum(my_list) / float(len(my_list))
# print(f"Average age of all people in list: {result}")



