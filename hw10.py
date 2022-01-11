# import block
import os
from datetime import datetime

# functions block
def get_domains_list_without_dot(dirname, filename_domains):
    domains_path = os.path.join(dirname, filename_domains)
    with open(domains_path, "r") as txt_file_domains:
        domains_data = txt_file_domains.read()
        domains_data = domains_data.replace(".", "")
        domains_data = domains_data.split("\n")
    return domains_data

def get_surnames_list_(dirname, filename_names):
    names_path = os.path.join(dirname, filename_names)
    with open(names_path, "r") as txt_file_names:
        names_data = txt_file_names.read()
        names_data = names_data.split("\n")
        names_data = [item.split() for item in names_data]
        names_data = [itm[1] for itm in names_data]
    return names_data

def get_dates_list(dirname, filename_authors):
    authors_path = os.path.join(dirname, filename_authors)
    with open(authors_path, "r") as txt_file_authors:
        authors_data = txt_file_authors.read()
        authors_data = authors_data.split("\n")
        authors_data = [elem[:(elem.find("-")-1)] for elem in authors_data if "-" in elem]
        return authors_data

def get_modified_dates_list(current_format, new_format, dates_list):
    authors_data_modified = []
    for itm in dates_list:
        itm = itm.split()
        itm[0] = ''.join(w_itm for w_itm in itm[0] if w_itm.isdigit())
        itm = " ".join(itm)
        itm = datetime.strptime(itm, "%d %B %Y")
        itm = datetime.strftime(itm, "%d/%m/%Y")
        authors_data_modified.append(itm)
    return authors_data_modified

def get_dictionaries_list(key_date, key_date_modified, dates_list, dates_list_modified):
    dict_dates = [{key_date: elem} for elem in dates_list]
    dict_dates_modified = [{key_date_modified: item} for item in dates_list_modified]
    dict_list = [{**elem_dict_d, **elem_dict_m} for elem_dict_d, elem_dict_m in zip(dict_dates, dict_dates_modified)]
    return dict_list

# functions call block
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
dirname = "Homeworks"
filename_domains = "domains.txt"
domains_list = get_domains_list_without_dot(dirname, filename_domains)
print(f"List of domains without dot: {domains_list}")

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
filename_names = "names.txt"
surnames_list = get_surnames_list_(dirname, filename_names)
print(f"List of surnames: {surnames_list}")

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
filename_authors = "authors.txt"
dates_list = get_dates_list(dirname, filename_authors)
current_format = "%d %B %Y"
new_format = "%d/%m/%Y"
dates_list_modified = get_modified_dates_list(current_format, new_format, dates_list)
key_date = "date_original"
key_date_modified = "date_modified"
dictionaries_list = get_dictionaries_list(key_date, key_date_modified, dates_list, dates_list_modified)
print(f"List of dictionaries with dates: {dictionaries_list}")





