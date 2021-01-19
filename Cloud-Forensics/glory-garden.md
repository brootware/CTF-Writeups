# Glory of the Garden

Point: 50

## Category

Forensics

## Question

This [garden](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg) contains more than it seems.

## Hint

What is a hex editor?

## Solution

As given in the hint, a hex editor is needed to read the hexadecimal contents of the jpeg file given. A VS Code plugin hex editor or online hex editor can be used to open the file and find the flag **"picoCTF{"**

## Improvement

2nd way to find the flag is to run the built-in ```xxd``` command on the jpeg file to read the contents of the file.
```console
xxd garden.jpg
```

3rd and the best way is to use the ```strings``` command and grep the flag.
```console
strings -a garden.jpg | grep pico
```