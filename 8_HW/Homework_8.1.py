from os import path

phonebookdb = "base.txt"
all_data = []
id = 0

if not path.exists(phonebookdb):
    with open(phonebookdb, "w", encoding="utf-8") as _:
        pass

def read_rec():
    global all_data, id, all_data_without_id
    with open(phonebookdb, encoding="utf-8") as f:

        all_data = [i.strip() for i in f]
        all_data_without_id = [i[2:] for i in all_data]
        if all_data:
            id = int(all_data[-1][0])

        return all_data

def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")

def create_contact():
    global id
    array = ["surname", "name", "surname_2", "phone_number"]
    string = ""

    for i in array:
        string += input(f"enter {i} ") + " "
    if all_data_without_id == []:
        id += 1
        with open(phonebookdb, "a", encoding="utf-8") as f:
            f.write(f"{id} {string}\n")
    else:
        string = string.strip()
        if string not in all_data_without_id:
            id += 1
            with open(phonebookdb, "a", encoding="utf-8") as f:
                f.write(f'{id} {string}\n')
        else:
            print("Этот контакт уже существует")

def search():
    search_value = input("Введите искомое значение: ")
    flag = False
    for string in all_data:
        string = string.split()
        for s in string:
            if search_value == s:
                print(*string)
                flag = True

    if flag == False:
        print("Такого контакта не существует")

def delete():
    delete_value = input("Введите удаляемое значение: ")
    flag = False
    for string in all_data:
        if delete_value == string[0]:
            f = open(phonebookdb, encoding="utf-8").read()
            a = f.replace(f"{string}\n", "")
            with open(phonebookdb, "w", encoding="utf-8") as f:
                f.write(a)
                flag = True
                print(a)
                break

    if flag == False:
        print("Нечего удалять")

def main_menu():
    play = True
    while play:
        read_rec()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete\n"
                       "5. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                create_contact()
            case "3":
                search()
            case "4":
                delete()
            case "5":
                play = False
            case _:
                print("Try again!\n")

main_menu()