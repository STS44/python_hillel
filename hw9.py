# import block
import random
import string
from string import ascii_lowercase

# functions block
def get_list_strings(my_list):
    list_strings = [item for item in my_list if type(item) == str]
    return list_strings

def get_list_contain_a(generate_list_strings):
    list_contain_a = [item for item in generate_list_strings if "a" in item]
    return list_contain_a

def get_list_first_a(generate_list_contain_a):
    list_first_a = [item for item in generate_list_contain_a if item[0] == "a"]
    return list_first_a

def get_list_symbols_str_occur_once(my_str):
    list_symbols_occur_once = [symbol for symbol in my_str if my_str.count(symbol) == 1]
    return list_symbols_occur_once

# task 5
def get_list_common_symbols(first_str, second_str):
    list_common_symbols = [symbol for symbol in first_str if symbol in second_str]
    return list_common_symbols

def get_list_unique_common_symbols(first_str, second_str):
    generate_list_common_symbols = get_list_common_symbols(first_str, second_str)
    generate_list_common_symbols = list(set(generate_list_common_symbols))
    return generate_list_common_symbols

# variant 2
def get_common_symbols(first_str, second_str):
    generate_common_symbols = list(set(first_str).intersection(set(second_str)))
    return generate_common_symbols

# task 6
def get_string_first_symbols_occur_once(string_first):
    list_string_first = [symbol for symbol in string_first if string_first.count(symbol) == 1]
    string_first = "".join(list_string_first)
    return string_first

def get_string_second_symbols_occur_once(string_second):
    list_string_second = [symbol for symbol in string_second if string_second.count(symbol) == 1]
    string_second = "".join(list_string_second)
    return string_second

def get_list_intersected_symbols_occur_once(string_first, string_second):
    generate_new_string_first = get_string_first_symbols_occur_once(string_first)
    generate_new_string_second = get_string_second_symbols_occur_once(string_second)
    list_intersected_symbols = [element for element in generate_new_string_first if element in
                                generate_new_string_second]
    return list_intersected_symbols

# variant 2
def get_common_symbols(string_first, string_second):
    generate_common_symbols = list(set(string_first).intersection(set(string_second)))
    return generate_common_symbols

def get_common_unique_symbols(string_first, string_second):
    new_list = []
    for symbol in get_common_symbols(string_first, string_second):
        if string_first.count(symbol) == string_second.count(symbol) == 1:
            new_list.append(symbol)
    return new_list

# task 7
def get_random_int_str_format(min_integer, max_integer):
    random_int_str_format = str(random.randint(min_integer, max_integer))
    return random_int_str_format
def get_random_string(min_length, max_length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for item in range(random.randint(min_length, max_length)))
    return random_string
def generate_email(names, domains):
    generate_random_int_str_format = get_random_int_str_format(min_integer, max_integer)
    generate_random_string = get_random_string(min_length, max_length)
    choose_name_randomly = "".join(random.choice(names))
    choose_domain_randomly = "".join(random.choice(domains))
    email_str = f"e-mail: {choose_name_randomly}.{generate_random_int_str_format}@{generate_random_string}." \
                f"{choose_domain_randomly}"
    return email_str

# variant 2

def get_email(domains, names):
    name = random.choice(names)
    domain = random.choice(domains)
    len_str = random.randint(5, 7)
    rand_int = random.randint(100, 999)
    rand_str = "".join([random.choice(ascii_lowercase) for _ in range(len_str)])
    e_mail = f"{name}.{rand_int}@{rand_str}.{domain}"
    return e_mail

# functions call block
# 3. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33, "one"]
# Функция возвращает новый список в котором содержаться только строки из my_list.
my_list = ["advertising", "111111", "conventional", "architecture", "parking", "22222", 3333, 444, 55, 6]
generate_list_strings = get_list_strings(my_list)
print(f"list of strings: {generate_list_strings}")

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
generate_list_contain_a = get_list_contain_a(generate_list_strings)
print(f"list of strings with symbol 'a' anywhere: {generate_list_contain_a}")

# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
generate_list_first_a = get_list_first_a(generate_list_contain_a)
print(f"list of strings with 1st symbol 'a': {generate_list_first_a}")

# 4. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
# Т.е. для строки "qqweeerrty" ответ должен быть ["w", "t", "y"]
my_str = "qqweeerrty"
generate_list_symbols_occur_once = get_list_symbols_str_occur_once(my_str)
print(f"list of symbols that occur in the string only once: {generate_list_symbols_occur_once}")

# 5. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# Т.е. для строк "qqwwerrttyy" и "qweeeeeee123" ответ должен быть ["q", "w", "e"]
first_str = "qqwwerrttyy"
second_str = "qweeeeeee123"
generate_list_unique_common_symbols = get_list_unique_common_symbols(first_str, second_str)
print(f"list of symbols that occur in both strings at least once: {generate_list_unique_common_symbols}")

# variant 5
result_5 = get_common_symbols(first_str, second_str)
print(f"List of common symbols: {result_5}")

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
# Т.е. для строк "qwwwwerrrrtyyyy" и "qweeeeeeerty123" ответ должен быть ["q", "t"]
string_first = "qwwwwerrrrtyyyy"
string_second = "qweeeeeeerty123"
generate_list_intersected_symbols_occur_once = get_list_intersected_symbols_occur_once(string_first, string_second)
print(f"list of symbols common for both strings and occur only once in each : "
      f"{generate_list_intersected_symbols_occur_once}")

# variant 2
result_6 = get_common_unique_symbols(string_first, string_second)
print(f"list of common symbols that occur once in each string : "
      f"{result_6}")

# 7*. Даны списки names и domains (создать самостоятельно).
# Написать функцию create_email для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Пример использования функции:
names = ["king", "miller", "kean", "smith", "ironman", "press"]
domains = ["net", "com", "ua", "org", "uk", "io"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
min_length = 5
max_length = 7
min_integer = 100
max_integer = 999
create_email = generate_email(names, domains)
print(create_email)

# variant 2
result_7 = get_email(domains, names)
print(result_7)










