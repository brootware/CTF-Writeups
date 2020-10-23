# The numbers

Point: 50

## Category

Cryptography

## Question

The [numbers](https://2019shell1.picoctf.com/static/eb3589c566dd3f809908053460acb817/the_numbers.png) [(link)](https://2019shell1.picoctf.com/static/eb3589c566dd3f809908053460acb817/the_numbers.png)... what do they mean?

## Hint

The flag is in the format PICOCTF{}

## Solution

A picture of the numbers in PNG format is given to be downloaded as such the numbers are as below.

```bash
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
```

From the pattern above it is quite obvious that this is in the PICOCTF{FLAG} format. The numbers are then decoded using an online Letter to Number A1Z26 Converter.

## Improvement

A quick python script can be written to quickly replace all the numbers with letters vice versa.