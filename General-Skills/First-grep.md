# First Grep

Point: 100

## Category

General Skills

## Question

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Hint

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution

```bash
wget https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file

cat file | grep picoCTF{ > flag.txt
```

## Improvement

None