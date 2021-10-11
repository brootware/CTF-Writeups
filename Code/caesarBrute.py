#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Oaker Min - https://github.com/Brucius"
__version__ = "0.1.0"
__license__ = "MIT"


def caesar(uInput):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(letters)):
        translated = ''
        for symbol in uInput:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + symbol
        print("picoCTF{%s}" % translated)


def main():
    """ Main entry point of the app """
    uInput = input("Key in your caesar encrypted message : ")
    caesar(uInput)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
