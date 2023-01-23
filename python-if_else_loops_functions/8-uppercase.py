#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for letter in str:
        letter_code = ord(letter)
        if (letter_code >= 97 and letter_code <= 122):
            upper_str += chr(letter_code - 32)
        else:
            upper_str += letter
    print("{}".format(upper_str))
