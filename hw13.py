# import block
import requests
import csv

# functions block
# task 1
url = "http://api.forismatic.com/api/1.0/"

def sort_by_quoteAuthor(item):
    quoteAuthor = item['quoteAuthor']
    return quoteAuthor

def get_sorted_unique_quotes_authored_list(quotes_number):
    unique_quotes_authored_list = []
    params = {"method": "getQuote", "format": "json", "lang": "ru", "key": [idx for idx in range(quotes_number)]}
    while len(unique_quotes_authored_list) < quotes_number:
        response = requests.get(url, params=params)
        response = response.json()
        response = {key: response[key] for key in keys}
        if not response['quoteAuthor']:
            continue
        if response['quoteText'] not in [quote['quoteText'] for quote in unique_quotes_authored_list]:
            unique_quotes_authored_list.append(response)
    sorted_unique_quotes_authored_list = sorted(unique_quotes_authored_list, key=sort_by_quoteAuthor)
    return sorted_unique_quotes_authored_list

# task 2
def create_and_write_csv_file(result_1, filename="quotes.csv"):
    with open(filename, "w") as csv_file:
        fieldnames = result_1[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(result_1)

# functions call block
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.
quotes_number = 10
keys = ['quoteAuthor', 'quoteText', 'quoteLink']
result_1 = get_sorted_unique_quotes_authored_list(quotes_number)
print(result_1)

# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
create_and_write_csv_file(result_1)






