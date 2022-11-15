# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с
малыми буквами). Определите декоратор для этой функции, который имеет один параметр
tag , определяющий строку с названием тега (начальное значение параметра tag равно
h1 ). Этот декоратор должен заключать возвращенную функцией строку в тег tag и
возвращать результат. Пример заключения строки "python" в тег h1: <h1>python</h1> .
Примените декоратор со значением tag="div" к функции и вызовите декорированную
функцию. Результат отобразите на экране.
"""

def intag(tag="h1"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            obj = func(*args, **kwargs)
            print(f"<{tag}>{obj}</{tag}>")
        return wrapper
    return decorator


@intag(tag="div")
def lowcase(strok):
    return strok.lower()


if __name__ == '__main__':
    s = input("Введите строку:\n")
    lowcase(s)
