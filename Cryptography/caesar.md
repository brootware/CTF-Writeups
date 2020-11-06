# caesar

Point: 100

## Category

Cryptography

## Question

Decrypt this [message](https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext).

## Hint

caesar cipher [tutorial](https://privacycanada.net/classical-encryption/caesar-cipher/)

## Solution

A text file with cipher text is given to download. The important part of the caesar cipher tutorial is on the mathematical algorithm to encrypt and decrypt.

```console
picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
```

Encryption algorithm
![image](https://mk0privacycanadehyf0.kinstacdn.com/wp-content/uploads/2020/01/enx.png)

In plain terms, this means that the encryption of a letter x is equal to a shift of x + n, where n is the number of letters shifted. The result of the process is then taken under modulo division, essentially meaning that if a letter is shifted past the end of the alphabet, it wraps around to the beginning.

Decryption algorithm
![image](https://mk0privacycanadehyf0.kinstacdn.com/wp-content/uploads/2020/01/dnx.png)

Decryption of the encrypted text (called the ciphertext) would be carried out similarly, subtracting the shift amount.

With some help of google and useful resources such as [this](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm). A quick python script is written as below to bruteforce and decrypt the cipher text for all 26 combinations.

```python
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
```

Run the program as below and input the encrypted message.
```console
python3 caesar.py
Key in your caesar encrypted message : gvswwmrkxlivyfmgsrhnrisegl
picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
picoCTF{furvvlqjwkhuxelfrqgmqhrdfk}
picoCTF{etquukpivjgtwdkeqpflpgqcej}
picoCTF{dspttjohuifsvcjdpoekofpbdi}
```

It should be fairly easy to spot the flag from the 26 combinations that python script prints out.

## Improvement

The python script written can only handle lower case letters and will not work if there's an upper case.