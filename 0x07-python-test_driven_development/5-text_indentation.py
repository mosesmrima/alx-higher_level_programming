#!/usr/bin/env python3

""" This module contains one function to indent text """


def text_indentation(text):
    """
    text_indentation: indent tex
    @text: the text to indent
    Return: no return value
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == " ":
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == " ":
                c += 1
            continue
        c += 1
