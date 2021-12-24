import random

# tuples, multitudes

# Task 1 Transform list to tuple
LIST_SIZE = 10
RANDOM_LOWER_BOUND = -5
RANDOM_UPPER_BOUND = 15
my_list = []
for item in range(LIST_SIZE):
    my_list.append(random.randint(RANDOM_LOWER_BOUND, RANDOM_UPPER_BOUND))
print(f"my list {my_list}")
my_tuple = tuple(my_list)
print(f"my tuple {my_tuple}")

# Task 2 Change the last item of tuple in list
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f"Sample list: {sample_list}")
result = [new_list[:-1] + (100,) for new_list in sample_list]
print(f"Actual result: {result}")
exp_output = [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
assert result == exp_output, f"FAILED expected output: {exp_output}, actual {result}"

# Task 3 Variant 1
tuple_1 = (1, 2, 3, 4)
tuple_2 = (3, 5, 2, 1)
tuple_3 = (2, 2, 3, 1)
list_of_tuples = [tuple_1, tuple_2, tuple_3]
zipped = list(zip(*list_of_tuples))
res_tuple = (sum(zipped[0]), sum(zipped[1]), sum(zipped[2]), sum(zipped[3]))
print(f"Item-by-item sum tuples: {res_tuple}")
exp_tuple = (6, 9, 8, 6)
assert res_tuple == exp_tuple, f"FAILED expected output: {exp_tuple}, actual {res_tuple}"

# Task 3 Variant 2
sum_items_list = []
for i_zip in zipped:
    sum_items = 0
    for item in i_zip:
        sum_items += item
    sum_items_list.append(sum_items)
result = tuple(sum_items_list)
print(f"Item-by-item sum : {result}")
assert result == exp_tuple, f"FAILED expected result: {exp_tuple}, actual {result}"

# Task 4 if Value is in set or not
my_set = frozenset({1.05, 2.33, 3.14, 5.75, 13, 22, 100, -5, -1.9, 0})
input_value = float(input("Enter number: "))
if input_value in my_set:
    print(f"Number is in set")
else:
    print(f"Number isn't in set")

# Task 5 Variant 1
set_1 = {123, -55, 0.33, 404, 0, -8.67, 6.25, 602, -0.88, 78, 55}
set_2 = {-33, 142, 44, -123, 303, -45, 6.2567, 100, -1.34, 55}
result = set_1.isdisjoint(set_2)
print(f"Two sets don't have common items: {result}")

# Task 5 Variant 2
intersect = set_1 & set_2
if intersect == set():
    print(f"Two sets don't have common items")
else:
    print(f"Two sets have common items")

# Task 6 Search of items in set A that aren't in set B
set_A = frozenset({123, -55, 0.33, 404, 0, -8.67, 6.25, 602, -0.88, 78})
set_B = frozenset({6.25, 602, -0.88, 78, 303, -45, 6.2567, 100, -1.34, 55})
result_A_B = set_A.difference(set_B)
print(f"set A - set B: {result_A_B}")

# Task 7 Delete Intersection of set_2 from set_1
set_1 = {123, -55, 0.33, 404, 0, -8.67, 6.25, 602, -0.88, 78}
print(f"set 1 : {set_1}")
set_2 = {-33, 142, 44, 123, 0, -45, 6.25, 100, -1.34, -55}
print(f"set 2 : {set_2}")
intersect = set_1.intersection(set_2)
for elem in intersect:
    set_1 -= intersect
intersect.clear()
print(f"Updated Set_1: {set_1}")

# Task 8 Union for two lists. Check algorithm on set.union
list_1 = [11, 23, 0, -9, 25, 875, -9, 25, -40, 23]
print(f"List 1: {list_1}")
list_2 = [105, 679, -15, 367, 875, -40, 33, 47, 0, 2, -15, 0]
print(f"List 2: {list_2}")
union_list_dup = []
for elem in list_1:
    union_list_dup.append(elem)
for item in list_2:
    if item not in list_1:
        union_list_dup.append(item)
union_list_unique = []
for itm in union_list_dup:
    if itm not in union_list_unique:
        union_list_unique.append(itm)
print(f"Union for lists: {union_list_unique}")

# Check
set_1 = set(list_1)
set_2 = set(list_2)
union_set = set_1.union(set_2)
assert set(union_list_unique) == union_set, f"FAILED expected: {union_set}, actual {union_list_unique}"

# Task 9 Difference for two lists. Check algorithm on set.difference
list_a = [13, -5, 78, -45, 0, 33, 100, -2, 0, 78]
print(f"List a: {list_a}")
list_b = [-5, 78, -45, 125, 340, 1000, 340]
print(f"List b: {list_b}")
list_diff_ab = []
for itm in list_a:
    if itm not in list_b:
        list_diff_ab.append(itm)
list_diff_ab_unique = []
for elm in list_diff_ab:
    if elm not in list_diff_ab_unique:
        list_diff_ab_unique.append(elm)
print(f"Difference of lists a and b: {list_diff_ab_unique}")
list_diff_ba = []
for item in list_b:
    if item not in list_a:
        list_diff_ba.append(item)
list_diff_ba_unique = []
for elem in list_diff_ba:
    if elem not in list_diff_ba_unique:
        list_diff_ba_unique.append(elem)
print(f"Difference of lists b and a: {list_diff_ba_unique}")

# Check
set_a = set(list_a)
set_b = set(list_b)
diff_set_ab = set_a.difference(set_b)
diff_set_ba = set_b.difference(set_a)
assert set(list_diff_ab_unique) == diff_set_ab, f"FAILED DIFF a and b expected: {diff_set_ab}, " \
                                                f"actual {list_diff_ab_unique}"
assert set(list_diff_ba_unique) == diff_set_ba, f"FAILED DIFF b and a expected: {diff_set_ba}, " \
                                                f"actual {list_diff_ba_unique}"
