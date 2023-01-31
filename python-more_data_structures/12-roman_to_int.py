#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    if (not roman_string or type(roman_string) != str):
        return total
    for i in range(len(roman_string) - 1, -1, -1):
        num_roman = roman[roman_string[i]]
        if (4 * num_roman < total):
            total -= num_roman
        else:
            total += num_roman
    return total
