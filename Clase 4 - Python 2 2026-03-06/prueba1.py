import os
from time import sleep

def decorator2(item="1"):
    def redecorator(function):
        def refunction():
            if item == "0":
                return "Hello Yui++"
            else:
                return "Hello Kana"
        return refunction
    return redecorator

def decorator(function):
    def intermediate():
        return function().upper()
    return intermediate

@decorator
def print_kimi():
    return "kimi"

@decorator2("1")
def say_hello():
    return "Kimi"

arrow_function = lambda item : "Is digit" if str(item).isdigit() else "Is not digit"

print(print_kimi())

print(print_kimi.__name__)
print(print_kimi.__doc__)

print(say_hello())
print(arrow_function(7))

