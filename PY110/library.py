"""
This is a module for working with the library catalog.
It has the ability to search the directory.
Save the directory to an external JSON file and also receive new information from external files.
"""
import json


catalog: dict = {"books": ["New Python", "How work on Python", "Sherlock Holmes", "Dog`s life", "Work at home"],
           "author": ["J. Basc", "J. Basc", "Arthur Conan Doyle", "Mark Twen", "A. Peters"],
           "genre": ["IT", "IT", "Detective", "Roman", "Lifestyle"],
           "description": ["Интересная книга", "Очень интересная книга", "Занимательное чтиво", "Советую почитать", "Ла-ла-ла"]}
row_bibl: list = []


def w_file(*args: dict) -> json:
    """
    This function saves the directory in a JSON file.
    :param args: Catalog dictionary.
    :return: JSON file.
    """
    with open("catalog.json", "w") as f:
        for i in args:
            json.dump(i, f)
        print("Готово")


def load_cat() -> dict:
    """
    This function reads a JSON file.
    :return: Information from a JSON file.
    """
    with open("catalog.json", "r") as f:
        jf = json.load(f)
        print("Готово")
    return jf


def add_book():
    """
    This function adds a new book to the catalog.
    :return: None
    """
    global catalog
    book = input("Введите название книги ")
    author = input("Введите ФИО автора ")
    genre = input("Введите наименование жанра книги ")
    description = input("Введите описание книги ")
    catalog['books'].append(book)
    catalog['author'].append(author)
    catalog['genre'].append(genre)
    catalog['description'].append(description)
    print("Готово")



def delete_book():
    """
    This function removes a book from the catalog.
    :return: None
    """
    global catalog
    ind = int(input("Введите номер книги, которую желаете удалить "))
    if ind - 1 <= len(catalog['books']):
        del catalog['books'][ind - 1]
        del catalog['author'][ind - 1]
        del catalog['genre'][ind - 1]
        del catalog['description'][ind - 1]
        print("Готово")
    else:
        print("Книги под таким номером не существует")


def biblioteka() -> list:
    """
    This function forms a visual representation of books in the catalog.
    :return: Book list.
    """
    b = []
    for i in range(len(catalog['books'])):
        b.append(f"Book \"{catalog['books'][i]}\", {catalog['author'][i]}. Genre: {catalog['genre'][i]}")
    return b

def finder(word: str):
    """
    This is a book search feature by keyword.
    :param word:Some word to search.
    :return: None
    """
    global row_bibl
    t = 0
    for i in range(len(row_bibl)):
        if row_bibl[i].find(word) != -1:
            t += 1
            print((i + 1), row_bibl[i])
    if not t:
        print("По данному запросу ничего не найдено")

def some_description():
    """
    This function shows the description in the selected book.
    :return: None
    """
    global catalog
    ind = int(input("Введите номер книги, описание которой хотите прочитать "))
    if ind - 1 <= len(catalog['books']):
        print(catalog['description'][ind - 1])
    else:
        print("Книги под таким номером не существует")

def change_description():
    """
    This function changes the description in the selected book.
    :return: None
    """
    global catalog
    ind = int(input("Введите номер книги, описание которой хотите изменить "))
    if ind - 1 <= len(catalog['books']):
        row = input("Введите свое описание книги ")
        catalog['description'][ind - 1] = row
        print("Готово")
    else:
        print("Книги под таким номером не существует")


def work_in_bib():
    """
    This function is for working with the library.
    :return: None
    """
    global row_bibl
    row_bibl = biblioteka()
    for i in enumerate(row_bibl, 1):
        print(i)
    print("A. Добавить книгу", "B. Удалить книгу", "C. Прочитать описание книги",
          "D. Изменить описание книги", "E. Вернуться назад")
    usl = input("Введите букву обозначающую действие над библиотекой ")
    if usl == "A":
        add_book()
    elif usl == "B":
        delete_book()
    elif usl == "C":
        some_description()
    elif usl == "D":
        change_description()
    elif usl == "E":
        p = 0
    else:
        print("Не корректная команда")


def start():
    """
    The main function for working with the module, collects all the functions.
    :return: None
    """
    global row_bibl
    global catalog
    print("MY OWN LIBRARY")
    print()
    row_bibl = biblioteka()
    p = 0
    while p != 5:
        try:
            m = ["Открыть библиотеку", "Поиск в билиотеке", "Выгрузить каталог", "Загрузить внешний каталог", "Выход"]
            for i in enumerate(m, 1):
                print(i)
            p = int(input("Введите от 1 до 5 для выполнения действия "))
            if p == 1:
                work_in_bib()
            elif p == 2:
                s = input("Введите ключевое слово для поиска ")
                finder(s)
            elif p == 3:
                w_file(catalog)
            elif p == 4:
                catalog = load_cat()
        except Exception:
            print("Не корректная команда")
            start()


if __name__ == '__main__':
    start()