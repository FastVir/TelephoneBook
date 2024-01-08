import os, re


def phone_format(n):  # форматирование телефонного номера
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):  # Функция вывода телефонной книги в консоль
    telephoneBook = []
    splitLine = "=" * 50
    print(splitLine)
    print(" №  Фамилия         Имя         Номер телефона")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        telephoneBook.append(
            {
                "ID": personID,
                "lastName": lastName,
                "name": name,
                "phone": phone_format(phone),
            }
        )
        personID += 1

    for contact in telephoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10}  {phone:<15}")

    print(splitLine)


def showContacts(fileName):  # Функция открытия телефонной книги
    os.system("cls")
    telephoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- нажмите любую клавишу ---")


def addContact(fileName):  # Функция добавления нового контакта в телефонную книгу
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию: ") + ","
        res += input("Введите имя: ") + ","
        res += input("Введите номер телефона: ")

        file.write(res + "\n")

    input("\nКонтакт успешно добавлен!\n--- нажмите любую клавишу ---")


def findContact(fileName):  # Функция поиска контактов в телефонной книге
    os.system("cls")
    target = input("Введите значение для поиска контакта: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"Нет контакта с таким значением '{target}'.")

    input("--- нажмите любую клавишу ---")


def changeContact(fileName):  # Функция изменения информации в контакте
    os.system("cls")
    telephoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите Номер контакта для изменения или 0 для возврата в Главное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введитете новое имя: ")
            newPhone = input("Введите новый номер телефона: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт успешно изменен!")
                input("\n--- нажмите любую клавишу ---")
        else:
            return


def deleteContact(fileName):  # Функция удаления контакта из телефонной книги
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите Номер контакта для удаления или 0 для возврата в Главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаленная запись: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- нажмите любую кнопку ---")


def showInterface():  # Интерфейс главного меню
    print('\033[1m' + "     ТЕЛЕФОННЫЙ СПРАВОЧНИК      " + '\033[0m')
    print("=" * 30)
    print('\033[1m' + "[1]" + '\033[0m' + " -- Показать контакты")
    print('\033[1m' + "[2]" + '\033[0m' + " -- Добавить контакт")
    print('\033[1m' + "[3]" + '\033[0m' + " -- Найти контакт")
    print('\033[1m' + "[4]" + '\033[0m' + " -- Изменить контакт")
    print('\033[1m' + "[5]" + '\033[0m' + " -- Удалить контакт")
    print('\n' + '\033[1m' + "[0]" + '\033[0m' " :  -- Выход")
    print("=" * 30)


def main(file_name):  # Главное меню
    while True:
        os.system("cls")
        showInterface()
        userChoice = int(input("Введите число от 1 до 5 из списка выше либо 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо!")
            return


path = "telephoneBook.txt"

main(path)