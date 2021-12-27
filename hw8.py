# import block
import random

# functions block
def generate_rand_int_and_print():
    number = random.randint(1, 100)
    print(f"Random integer number in range [1, 100): {number}")

def get_rand_int():
    int_num = random.randint(1, 100)
    return int_num

def generate_rand_int_and_print_word():
    rand_int = random.randint(1, 100)
    if rand_int > 50:
        print("Хорошо")
    else:
        print("Плохо")

def print_some_str_upper(some_str):
    some_str = some_str.upper()
    print(f"String in the UPPERCASE: {some_str}")

some_str = "qwerty"

def get_some_str_upper(some_string):
    some_string = some_string.upper()
    return some_string

some_string = "hello world!"

def get_list_str_upper(list_str):
    list_str = [item.upper() for item in list_str]
    return list_str

list_str = ["lll", "iii", "sss", "ttt"]

def get_list_number(upper_bound):
    list_number = [num for num in range(1, upper_bound+1)]
    return list_number

upper_bound = 20

def get_square_number(upper_bnd):
    list_square_num = [number**2 for number in range(1, upper_bnd+1)]
    return list_square_num

upper_bnd = 10

# Functions call block
# 1. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает его.
generate_rand_int_and_print()
# 2. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и возвращает его.
rand_int = get_rand_int()
print(f"Random integer number in range [1, 100): {rand_int}")
# 3. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает слово
# "Хорошо", если это число больше 50 или слово "Плохо" в противоположном случае.
generate_rand_int_and_print_word()
# 4. Написать функцию, которая принимает в качестве параметра строку и печатает ее в верхнем регистре (UPPERCASE).
print_some_str_upper(some_str)
# 5. Написать функцию, которая принимает в качестве параметра строку и возвращает ее в верхнем регистре (UPPERCASE).
new_string = get_some_str_upper(some_string)
print(f"String in the UPPERCASE: {new_string}")
# 6. Написать функцию, которая принимает в качестве параметра список строк и возвращает их в виде списка строк
# в верхнем регистре (UPPERCASE).
new_list = get_list_str_upper(list_str)
print(f"List of strings in the UPPERCASE: {new_list}")
# 7. Написать функцию, которая принимает в качестве параметра число и возвращает список чисел от 1
# до заданного числа включительно.
generated_list_num = get_list_number(upper_bound)
print(f"List of numbers in range [1, given number]: {generated_list_num}")
# 8. Написать функцию, которая принимает в качестве параметра число и возвращает список квадратов чисел от 1
# до заданного числа включительно.
generated_list_square_num = get_square_number(upper_bnd)
print(f"List of square numbers in range [1, given number]: {generated_list_square_num}")