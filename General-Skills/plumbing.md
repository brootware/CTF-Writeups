# plumbing

Point: 200

## Category

General skills

## Question

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 4427

## Hint

Remember the flag format is picoCTF{XXXX}
What's a pipe? No not that kind of pipe... This kind

## Solution

This challenge is very simple if you're familiar with Linux command line for piping and grabbing specific keywords. Below command grabs the flag that the URL outputs.

```
nc jupiter.challenges.picoctf.org 4427 | grep pico 
```


## Improvement
None
