# strings it

Point: 100

## Category

General Skills

## Question

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

## Hint

[strings](https://linux.die.net/man/1/strings)

## Solution

```bash
stings strings -a | grep picoCTF{ > flag.txt
```

## Improvement

None