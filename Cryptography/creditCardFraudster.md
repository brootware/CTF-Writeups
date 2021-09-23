# The Credit Card Fraudster

Point: 20

## Category

Cryptography

## Question

I just arrested someone who is probably the most wanted credit card fraudster in Europe. She is a smart cybercriminal, always a step ahead INTERPOL and she kept unnoticed for years by never buying online, but buying goods with a different card every time and in different stores. My cyber-analysts found out after collecting all evidences she hacked into one the largest payment provider in Europe, reverse-engineered the software present on the server and partly corrupted the card number validation code to accept all her payments. The change enables acceptance of any transaction with a card number multiple of 123457 and the Luhn check digit is valid.

I caught her because every year she bought a bouquet of flowers next to the same cemetery. While handcuffing her at the flower shop's exit, she said the flowers were for her lost father and today it is his death anniversary. She broke down in tears and she did some steps and threw something in the sewers. My female colleague conducted a search on her, but she couldn't find the card she used, only the receipt.

The little flower shop
======================

European Express Debit
Card Number: 543210******1234
SALE

Please debit my account
Amount: 25.00€
Can you help me to recover the card number so that I can confirm with the flower merchant's bank the card number was used in that shop and is fraudulent?

## Hint

1/ Luhn_algorithm

2/ Flag format is CTFlearn{card_number}


## Solution

The problem scope is to try to guess the masked numbers of 543210******1234 for a valid credit card number. The number can be divisible by 123457 as the question stated which means n % 123457 == 0. 

The credit card numbers can be checked using [luhn's algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

Python has a pip module for luhn's algorithm implementation. A brute force approach is used to correctly guess the number with a simple python script below.

```python
import luhn

for i in range(5432100000001234, 5432109999991234, 10000):
    if i % 123457 == 0 and luhn.verify(str(i)):
        print("CTFlearn{{{}}}".format(i))
```

## Improvement
None