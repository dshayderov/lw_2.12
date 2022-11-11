# !/usr/bin/env python3
# -*- coding: utf-8 -*-


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
    s = input()
    lowcase(s)
