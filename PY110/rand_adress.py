"""
This is a module for generating random addresses, with the ability to read arguments from a json file
"""


import re
import random
import json
import numpy


country: list = ["Россия", "Украина"]
town: list = ["Тюмень", "Москва", "Сочи", "Новосибирск", "Анапа", "Екатеринбург"]
street: list = ["Коро!лева", "Яхтенная", "Мира", "Свердловская", "Весенняя", "Арктическая"]
some_test: list = ["test", "test"]
corp: list = ["", 1, 2, 3, "A", "B"]


def write_file(arg_a: list, arg_b: list, arg_c: list):
    """
    This function creates a json file
    :param arg_a: a list with country names
    :param arg_b: а list with town names
    :param arg_c: а list with street names
    """
    with open("зачет.json", "wt") as f:
        f.write(json.dumps({"country":arg_a, "town":arg_b, "street":arg_c}, ensure_ascii=False))


def load_file():
    """
    This function reads json file
    :return: three lists
    """
    with open("зачет.json") as f:
        w = json.load(f)
        if "country" in w:
            country_json = w['country']
        else:
            raise Exception("Wrong json file")
        if "street" in w:
            street_json = w['street']
        else:
            raise Exception("Wrong json file")
        if "town" in w:
            town_json = w['town']
        else:
            raise Exception("Wrong json file")
    return country_json, town_json, street_json


def contr_reg(*args, **kwargs):
    """
    This function checks list items for invalid characters
    :param args: a list with country names or street names and others
    :param kwargs: a list with country names or street names and others
    :return: returned args or kwargs
    """
    res = r"[!?.,]"
    for i in args:
        reg_c = any([re.findall(res, j) for j in i])
        if reg_c:
            raise Exception(f"the element in {i} have invalid characters")
        pass
    for i in kwargs.items():
        reg_c = any([re.findall(res, j) for j in i])
        if reg_c:
            raise Exception(f"the element in {i} have invalid characters")
        pass
    return args, kwargs


def arg_decorator(arg: str = "test"):
    """
    This is a decorator for checking functions
    :param arg: string "test"
    :return: if the string "test" is found in the elements of the submitted lists, the decorator will return None
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in args:
                if arg in i:
                    print(f"Вызвана функция {func} с параметрами test")
                    return None
            for i in kwargs.items():
                if arg in i:
                    print(f"Вызвана функция {func} с параметрами test")
                    return None
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@arg_decorator()
def new_adress(c: list, t: list, s: list, k: list):
    """
    This is the main function that generates random addresses.
    :param c: a list with country names
    :param t: a list with town names
    :param s: a list with street names
    :param k: a list with buildings
    :return: random address
    """
    contr_reg(c, t, s)
    while True:
        house = random.randint(1, 50)
        flat = random.randint(1, 300)
        r_corp = numpy.random.choice(k)
        r_country = numpy.random.choice(c)
        r_town = numpy.random.choice(t)
        r_street = numpy.random.choice(s)
        r_adress = f"{r_country}, г.{r_town}, ул.{r_street}, д.{house}, корп.{r_corp}, кв.{flat}"
        yield r_adress


if __name__ == '__main__':
    write_file(country, town, street)

    a, b, c = load_file()

    s = new_adress(a, b, c, corp)
    print(next(s))

    g = new_adress(country, town, street, corp)
    print(next(g))

    j = new_adress(some_test, town, street, corp)