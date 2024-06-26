from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue
    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Не валидная фамилия")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue        
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телофон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def del_data(file_name):
    last_name = input("Введите фамилию для удаления данных: ")
    res = read_file(file_name)
    i = 0
    flag = True
    for el in res:
        if el["Фамилия"] == last_name:
            res.pop(i)
            flag = False
        i += 1
    if flag:
        print("Такой фамилии нет")
        return
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def change_data(file_name):
    last_name = input("Введите фамилию для изменения данных: ")
    res = read_file(file_name)
    i = 0
    flag = True
    for el in res:
        if el["Фамилия"] == last_name:
            num = i
            flag = False
        i += 1
    if flag:
        print("Такой фамилии нет")
        return
    lst = get_info()
    res[num] = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'


def main():
    while True:
        command = input(f"Введите команду:\n" 
        f" q - выход \n w - запись данных \n r - вывод данных \n c - изменение данных \n d - удаление данных \n")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            for i in read_file(file_name):
                print(i)
        elif command == 'c':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            change_data(file_name)
        elif command == 'd':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            del_data(file_name)


main()