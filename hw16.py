# import block
import os
import random
import string
import json
import csv

# functions block
# task 1

class CreateDataForTxt:
    def __init__(self, min_len=100, max_len=1000):
        self.min_len = min_len
        self.max_len = max_len

    def _create_random_string(self):
        str_len = random.randint(self.min_len, self.max_len)
        letters_digits_whitespaces = "".join([string.ascii_letters, string.digits, string.whitespace])
        rand_str = "".join(random.choice(letters_digits_whitespaces) for str_item in range(str_len))
        return rand_str

# task 2

class CreateDataForJson:
    def __init__(self, string_len=5, min_int=-100, max_int=100, min_num=5, max_num=20):
        self.string_len = string_len
        self.min_int = min_int
        self.max_int = max_int
        self.min_num = min_num
        self.max_num = max_num

    def _create_random_key(self):
        random_key = "".join(random.choice(string.ascii_lowercase) for key_str_item in range(self.string_len))
        return random_key

    def _create_random_value(self):
        random_int = random.randint(self.min_int, self.max_int)
        random_float = random.random()
        random_bool = random.choice([True, False])
        random_value = random.choice([random_int, random_float, random_bool])
        return random_value

    def _create_random_dict(self):
        keys_num = random.randint(self.min_num, self.max_num)
        random_dict = {self._create_random_key(): self._create_random_value() for dict_item in range(keys_num)}
        return random_dict

# task 3

class CreateDataForCsv:
    def __init__(self, min_num_row_col=3, max_num_row_col=10, min_val=0, max_val=1):
        self.min_num_row_col = min_num_row_col
        self.max_num_row_col = max_num_row_col
        self.min_val = min_val
        self.max_val = max_val

    def _create_random_table(self):
        rows_num = random.randint(self.min_num_row_col, self.max_num_row_col)
        columns_num = random.randint(self.min_num_row_col, self.max_num_row_col)
        table_value = random.choice([self.min_val, self.max_val])
        table_list = [[table_value] * columns_num for table_item in range(rows_num)]
        return table_list

# task 4

class GenerateAndWriteFile(CreateDataForTxt, CreateDataForJson, CreateDataForCsv):
    def __init__(self, dirname, min_len=100, max_len=1000, string_len=5, min_int=-100, max_int=100,
                 min_num=5, max_num=20, min_num_row_col=3, max_num_row_col=10, min_val=0, max_val=1):
        CreateDataForTxt.__init__(self, min_len, max_len)
        CreateDataForJson.__init__(self, string_len, min_int, max_int, min_num, max_num)
        CreateDataForCsv.__init__(self, min_num_row_col, max_num_row_col, min_val, max_val)
        self.dirname = dirname
        self.__create_file_dir()

    def __create_file_dir(self):
        os.makedirs(self.dirname, exist_ok=True)

    def _create_absolute_file_path(self):
        relative_file_path = os.path.join(self.dirname, filename)
        absolute_file_path = os.path.abspath(relative_file_path)
        return absolute_file_path

    def create_and_write_txt_file(self):
        with open(self._create_absolute_file_path(), "w") as new_txt_file:
            new_txt_file.write(self._create_random_string())

    def create_and_write_json_file(self):
        with open(self._create_absolute_file_path(), "w") as new_json_file:
            json.dump(self._create_random_dict(), new_json_file, indent=1)

    def create_and_write_csv_file(self):
        with open(self._create_absolute_file_path(), "w") as new_csv_file:
            table_writer = csv.writer(new_csv_file, delimiter=";")
            table_writer.writerows(self._create_random_table())

    def generate_and_write_file(self):
        self.__create_file_dir()
        if "txt" in self._create_absolute_file_path():
            self.create_and_write_txt_file()
        elif "json" in self._create_absolute_file_path():
            self.create_and_write_json_file()
        elif "csv" in self._create_absolute_file_path():
            self.create_and_write_csv_file()
        else:
            print(f"Unsupported file format")

# functions call block
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.

# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.

# Функция 4. Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
dirname ="Homework16Task4"
filename = "task4.pdf"
result = GenerateAndWriteFile(dirname)
result.generate_and_write_file()




