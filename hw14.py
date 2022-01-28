# import block
import re
import os
import json

# functions block
# task 1
def read_data_from_json(dirname, filename):
    file_path = os.path.join(dirname, filename)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

# task 2
def sort_by_surname(item):
    surname = "".join(item["name"].split()[-1])
    return surname

# task 3
def sort_by_years_of_death(item, pattern = r"[0-9]+"):
    if "BC" in item["years"]:
        year_of_death = -1 * int(re.findall(pattern, item["years"])[-1])
    else:
        year_of_death = int(re.findall(pattern, item["years"])[-1])
    return year_of_death

# task 4
def sort_by_number_of_words(item):
    number_of_words = len(item["text"].split())
    return number_of_words

# task 5
def create_and_write_json_file(dirname, new_filename, param, read_json_file):
    keys_param = {"name": sort_by_surname, "years": sort_by_years_of_death, "text": sort_by_number_of_words}
    sorted_data = sorted(read_json_file, key=keys_param[param])
    new_file_path = os.path.join(dirname, new_filename)
    with open(new_file_path, "w", encoding="utf-8") as new_json_file:
        json.dump(sorted_data, new_json_file, indent=1, ensure_ascii=False)

# functions call block

# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
dirname = "Homeworks"
filename = "data.json"
read_json_file = read_data_from_json(dirname, filename)
print(read_json_file)

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

# 4. Написать функцию сортировки по количеству слов в поле "text"

# 5. Написать функцию для записи отсортированных данных в файл. Параметры - имя файла для записи, параметр сортировки.
# Пример использования:
# write_json("new_data.json", "text")
param = "text"
new_filename = "new_data.json"
create_and_write_json_file(dirname, new_filename, param, read_json_file)





