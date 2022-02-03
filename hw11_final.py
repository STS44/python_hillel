# import block
import os
import random
import string
import json
import csv

# functions block
# task 1
def create_random_string(min_len=100, max_len=1000):
    str_len = random.randint(min_len, max_len)
    letters_digits_whitespaces = "".join([string.ascii_letters, string.digits, string.whitespace])
    rand_str = "".join(random.choice(letters_digits_whitespaces) for str_item in range(str_len))
    return rand_str

# task 2
def create_random_key(string_len=5):
    random_key = "".join(random.choice(string.ascii_lowercase) for key_str_item in range(string_len))
    return random_key

def create_random_value(min_int=-100, max_int=100):
    random_int = random.randint(min_int, max_int)
    random_float = random.random()
    random_bool = random.choice([True, False])
    random_value = random.choice([random_int, random_float, random_bool])
    return random_value

def create_random_dict(string_len=5, min_int=-100, max_int=100, min_num=5, max_num=20):
    keys_num = random.randint(min_num, max_num)
    random_int = random.randint(min_int, max_int)
    random_float = random.random()
    random_bool = random.choice([True, False])
    random_dict = {create_random_key(string_len=5): create_random_value(min_int=-100, max_int=100)
                   for dict_item in range(keys_num)}
    return random_dict

# task 3
def create_random_table(min_num_row_col=3, max_num_row_col=10, min_val=0, max_val=1):
    rows_num = random.randint(min_num_row_col, max_num_row_col)
    columns_num = random.randint(min_num_row_col, max_num_row_col)
    table_value = random.choice([min_val, max_val])
    table_list = [[table_value] * columns_num for table_item in range(rows_num)]
    return table_list

# task 4
def create_file_dir(dirname):
    os.makedirs(dirname, exist_ok=True)

def create_absolute_file_path(dirname, filename):
    relative_file_path = os.path.join(dirname, filename)
    return os.path.abspath(relative_file_path)

def create_and_write_txt_file(absolute_file_path):
    with open(absolute_file_path, "w") as new_txt_file:
        new_txt_file.write(create_random_string(min_len=100, max_len=1000))

def create_and_write_json_file(absolute_file_path):
    with open(absolute_file_path, "w") as new_json_file:
        json.dump(create_random_dict(string_len=5, min_int=-100, max_int=100, min_num=5, max_num=20),
                  new_json_file, indent=1)

def create_and_write_csv_file(absolute_file_path):
    with open(absolute_file_path, "w") as new_csv_file:
        table_writer = csv.writer(new_csv_file, delimiter=";")
        table_writer.writerows(create_random_table(min_num_row_col=3, max_num_row_col=10, min_val=0, max_val=1))

def generate_and_write_file(absolute_file_path, dirname):
    create_file_dir(dirname)
    if "txt" in absolute_file_path:
        create_and_write_txt_file(absolute_file_path)
    elif "json" in absolute_file_path:
        create_and_write_json_file(absolute_file_path)
    elif "csv" in absolute_file_path:
        create_and_write_csv_file(absolute_file_path)
    else:
        print(f"Unsupported file format")

# functions call block
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.
result_1 = create_random_string(min_len=100, max_len=1000)
print(result_1)

# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
result_2 = create_random_dict(string_len=5, min_int=-100, max_int=100, min_num=5, max_num=20)
print(result_2)

# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.
result_3 = create_random_table(min_num_row_col=3, max_num_row_col=10, min_val=0, max_val=1)
print(result_3)

# Функция 4. Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
dirname = "Homework11Task4"
filename = "task4.pdf"
absolute_file_path = create_absolute_file_path(dirname, filename)
result_4 = generate_and_write_file(absolute_file_path, dirname)





