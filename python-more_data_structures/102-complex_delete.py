#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_delete = [k for k, v in a_dictionary.items() if value == v]
    for key in keys_delete:
        del a_dictionary[key]
    return a_dictionary
