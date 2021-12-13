# lists, dictionaries
import random

# TASK1 REMOVE DUPLICATES FROM THE LIST
# LENGTH_LIST_DUPLICATES = 15
# LOWER_BOUND_LIST_DUPLICATES = 0
# UPPER_BOUND_LIST_DUPLICATES = 10
# list_duplicates = []
# for _ in range(LENGTH_LIST_DUPLICATES):
#     list_duplicates.append(random.randint(LOWER_BOUND_LIST_DUPLICATES, UPPER_BOUND_LIST_DUPLICATES))
# print("list with duplicates: {ld}".format(ld=list_duplicates))
# list_unique_num = []
# for num in list_duplicates:
#     if num not in list_unique_num:
#         list_unique_num.append(num)
# print("list with unique numbers: {lu}".format(lu=list_unique_num))

# TASK2 COPY LIST
# LENGTH_LIST_TO_COPY = 15
# LOWER_BOUND_LIST_TO_COPY = -10
# UPPER_BOUND_LIST_TO_COPY = 5
# list_to_copy = []
# for _ in range(LENGTH_LIST_TO_COPY):
#     list_to_copy.append(random.randint(LOWER_BOUND_LIST_TO_COPY, UPPER_BOUND_LIST_TO_COPY))
# print("list to copy: {ltc}".format(ltc=list_to_copy))
# list_copied = []
# for elem in list_to_copy:
#     list_copied.append(elem)
# print("copied list: {cl}".format(cl=list_copied))

# TASK 3 DIFF BETWEEN 2 LISTS
# LIST_LENGTH_A = 10
# LIST_LENGTH_B = 8
# UPPER_BOUND_A = 15
# LOWER_BOUND_A = -5
# UPPER_BOUND_B = 10
# LOWER_BOUND_B = -2
# list_a = []
# for _ in range(LIST_LENGTH_A):
#     list_a.append(random.randint(LOWER_BOUND_A, UPPER_BOUND_A))
# print("list a with random numbers: {a}".format(a=list_a))
# list_b = []
# for _ in range(LIST_LENGTH_B):
#     list_b.append(random.randint(LOWER_BOUND_B, UPPER_BOUND_B))
# print("list b with random numbers: {b}".format(b=list_b))
# list_diff_ab = []
# for i in list_a:
#     if i not in list_b:
#         list_diff_ab.append(i)
# print("difference between lists a and b: {ab}".format(ab=list_diff_ab))
# list_diff_ba = []
# for i in list_b:
#     if i not in list_a:
#         list_diff_ba.append(i)
# print("difference between lists b and a: {ba}".format(ba=list_diff_ba))

# TASK 4 UNION DICTIONARIES
# dict_1 = {1: 10, 2: 20}
# print("Dictionary 1: {d1}".format(d1=dict_1))
# dict_2 = {3: 30, 4: 40}
# print("Dictionary 2: {d1}".format(d1=dict_2))
# dict_3 = {5: 50, 6: 60}
# print("Dictionary 3: {d1}".format(d1=dict_3))
# dict_union = {}
# for key in (dict_1, dict_2, dict_3):
#     dict_union.update(key)
# print("Union dictionary: {ud}".format(ud=dict_union))

# TASK 5 CREATE DICTIONARY
# LOWER_BOUND_KEY = 1
# UPPER_BOUND_KEY = 16
# dictionary = {}
# for key in range(LOWER_BOUND_KEY, UPPER_BOUND_KEY):
#     dictionary[key] = key**2
# print("Dictionary: {d}".format(d=dictionary))
