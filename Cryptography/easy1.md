# Easy1

Point: 100

## Category

Cryptography

## Question

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt) to solve it?.

## Hint

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.

Please use all caps for the message.


## Solution

The way to solve this CTF is fairly straight forward when you figured out how key cipher works. To get some basic knowledge on key ciphers, picoctf has great primer on them. https://primer.picoctf.com/#_key_ciphers

Will just be going through the main mechanic of the key cipher in this write up using the example from the primer.

Let's say there's a plaintext
"ILOVEPITTSBURGH"

The key "PICOCTF" is used to encrypt. Since our text is larger than the key, we simply repeat the key several times until we get the same length in the following manner:

"PICOCTFPICOCTFP"

The first letter of the cleartext is paired with the first letter of the key. So, we have the pair ('I','P'). The table below can be used to find the intersection of row i and column p to find the encrypted letter. Same pattern is repeated for all the letters in the string.

In this case, our first letter is 'X'

![image](https://primer.picoctf.com/images/5image45.png)

To decrypt:
We take the first letter of the key, which is 'P', and go to that row in the vigenere table. Then in the row 'P', we find the first letter of the encrypted text, which is 'X'.The column that corresponds to 'X', is the first letter of the clear text, which in our case is 'I'. You repeat the same process for each character until you get the plaintext.

To automate this whole workflow, a quick python tool is written to encrypt and decrypt using the text and key. The tool can be found at
https://raw.githubusercontent.com/Brucius/picoCTF-tools/main/vignereCipher.py

Below is an example of running the program

```bash
wget https://raw.githubusercontent.com/Brucius/picoCTF-tools/main/vignereCipher.py

python3 vignereCipher.py


 Encrypt or Decrypt? 

 1) Encrypt 
 2) Decrypt 
 3) Quit 

 Your Choice : 2

Key in your ciphertext : UFJKXQZQUNB
Key in your cipher key : SOLVECRYPTO

SOLUTIONHERE
```

## Improvement

None