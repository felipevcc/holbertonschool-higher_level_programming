#!/usr/bin/python3
"""Function that indents text"""


def text_indentation(text):
    """String validation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """Separators"""
    sep = [".", "?", ":"]
    idx_prev = 0

    """Prints the text"""
    for i in range(len(text)):
        if i == len(text) - 1:
            print(text[idx_prev:i + 1], end="")
        elif text[i] in sep:
            print(text[idx_prev:i + 1] + '\n')
            idx_prev = i + 1
            """deletes spaces"""
            while text[idx_prev] == " ":
                idx_prev += 1
