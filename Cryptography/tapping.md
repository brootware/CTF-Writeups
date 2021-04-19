# Tapping

Point: 200

## Category

Cryptography

## Question

Theres tapping coming in from the wires. What's it saying ```nc jupiter.challenges.picoctf.org 48247```.


## Hint

What kind of encoding uses dashes and dots?

## Solution
First a netcat command given in the challenge description is ran in the terminal.

```console
% nc jupiter.challenges.picoctf.org 48247
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- }
```

A morse code is returned from the server. A python library called [morse-talk](https://github.com/morse-talk/morse-talk) is used to convert the dots and dashes to convert the encrypted message. The steps done are as below.

Install morse-talk using below command.
```console
% pip install morse-talk
```

The following python code is used to programmatically convert the morse code into plain text.
```python
import morse_talk as mdecode
code = ".--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- }"

## Special character braces are taken out from the morse code as the decoder doesn't handle the braces.
code=code.replace('{','')
code=code.replace('}','')

mdecode.decode(code)

'PICOCTFSOLUTIONHERE'
```

## Improvement

none