#!/usr/bin/python3
"""
<<<<<<< HEAD
    Insert here module comment
    Write a function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
    You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """ print my first and last name """
    str_error = "first_name must be a string or last_name must be a string"
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError(str_error)
    print("My name is", first_name, last_name)

=======
Print string
"""
def say_my_name(first_name, last_name=""):
   """Concatenate both parameters and print
   Parameters:
   first_name = first name
   last_name = last name
   Local Variables:
   fullname = empty string
   Return: None
   """
    fullname = ""
    if first_name and type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif first_name and type(first_name) == str:
        fullname += first_name + " "
    if last_name and type(last_name) != str:
        raise TypeError('last_name must be a string')
    elif last_name and type(last_name) == str:
        fullname += last_name
    print("My name is {:s}".format(fullname))
>>>>>>> 67c6bd079ffa0ebfb48ef2ae9bcd10f2d4c266a9
