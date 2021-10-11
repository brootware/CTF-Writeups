#!/usr/bin/env python3
"""
A quick hacky tool created for vignere encryption and decryption.
This was re-implemented using the original encryption and decryption written by user dssstr
https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4
"""

__author__ = "Oaker Min - https://github.com/Brucius"
__version__ = "0.1.0"
__license__ = "MIT"


def encrypt():
    plaintext = input("\nKey in your plaintext : ").upper().strip()
    key = input("Key in your cipher key : ").upper().strip()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    print("\n\n", ciphertext)


def decrypt():
    ciphertext = input("\nKey in your ciphertext : ").upper().strip()
    key = input("Key in your cipher key : ").upper().strip()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    print("\n\n", plaintext)


def menu():
    return int(input(
        "\n Encrypt or Decrypt? \n\n 1) Encrypt \n 2) Decrypt \n 3) Quit \n\n Your Choice : "))


def main():
    """ Main entry point of the app """
    while True:
        choice = menu()
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            print("\n Goodbye!")
            break


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
