# strings it

Point: 100

## Category

General Skills

## Question

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

## Hint

[strings](https://linux.die.net/man/1/strings)

## Solution

For this particular challenge, the file given is a 64-bit executable. There is a linux command ```file``` to find out the type of file from the command line.

So it is not as simple as doing a cat on the text file. The hint on using ```strings``` command is given to solve this flag.

```bash
wget https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings

file strings
strings: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0cdedfba33422d235dba8c90e00fb77b235f1ff8, not stripped

strings strings -a | grep picoCTF{ > flag.txt
```

## Improvement

None