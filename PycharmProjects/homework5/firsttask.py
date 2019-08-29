documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def find_people():
    numbers = input("Введите номер документа ")
    outs = "Нет такого документа "
    for document in documents:
        check = document["number"]
        if numbers == check:
           outs = document["name"]
    return print(outs)

def print_list():
    for document2 in documents:
        print(document2.values())

def find_shelf():
    numbers = input("Введите номер документа ")
    find = "Нет такого документа "
    for shelf, doc in directories.items():
        for counter in doc:
            if numbers == counter:
                find = shelf
    return print("Документ на полке ", find)

def add_document():
    types = input("Введите тип документа ")
    number = input("Введите номер документа ")
    name = input("Введите имя владельца документа ")
    shelf = input("На какую полку его поместить? ")
    document = {"type": types, "number": number, "name": name}
    documents.append(document)
    for shelfs, numb in directories.items():
        if shelf == shelfs:
            numb.append(number)
    return print(documents), print(directories)

def del_doc():
    number = input("Введите номер документа ")
    counter = -1
    for document in documents:
        counter += 1
        check = document["number"]
        if check == number:
            del(documents[counter])
    for shelf, doc in directories.items():
        counter = -1
        for count in doc:
            counter += 1
            if number == count:
                print(counter)
                directories[shelf].pop(counter)
                return print(documents), print(directories)

def move_doc():
    number = input("Введите номер документа ")
    move = input("Введите полку на которю переместить документ ")
    for shelf, doc in directories.items():
        count = -1
        for counter in doc:
            count += 1
            if number == counter:
                directories[shelf].pop(count)
        if shelf == move:
            directories[shelf].append(number)
            return print(documents), print(directories)
# for shelf, doc in directories.items():
#     print("11-2" in doc)
#     print("3" in shelf)
# пытался добавить код чтобы не сохранял неверные данные но пока наверное мне не хватает инструментов или мозгов

def add_shelf():
    shelh = input("Введите номер полки которую добавить ")
    polka = []
    directories.setdefault(shelh)
    return print(directories)

user_input = input("p - найти человека по номеру документа \nl - вывести весь список документов\
 \ns - Найти документ по номеру \na - Добавить документ \nd - Удалить документ \nm - Переместить документ \
  \nas - добавить полку\nВыберите команду ")

if user_input == "p":
    find_people()
elif user_input == "l":
    print_list()
elif user_input == "s":
    find_shelf()
elif user_input == "a":
    add_document()
elif user_input == "d":
    del_doc()
elif user_input == "m":
    move_doc()
elif user_input == "as":
    add_shelf()
else:
    print("Вы ввели неверную команду ")