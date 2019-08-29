import csv
from pprint import pprint
flats_list = list()

with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


# TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
# и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
counter = 0
for i, flat in enumerate(flats_list):
    if "новостройка" in flat:
        print(i, flat)
        counter += 1
print("Количество новостроек", counter)

# # TODO 2:
# # 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv:
# # ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
number = []
room = []
types = []
prices = []

for flat in flats_list:
    number.append(flat[0])
    room.append(flat[1])
    types.append(flat[2])
    prices.append(flat[11])
flat_info = {"id": number, "rooms": room, "type": types, "price": prices}
pprint(flat_info)
#
# # 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список
# # ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1
subway_dict = {}
list_counter = []
counter = 0
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    list_counter = [flat[0], flat[1], flat[2], flat[11]]
    counter += 1
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append(list_counter)
pprint(subway_dict)

# # 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.

subway_dict = {}
counter = 0
for flat in flats_list:
    subway = flat[3].replace("м.", "У метро ")
    counter += 1
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
        subway_dict[subway].append(counter)
        counter = 0
pprint(subway_dict)