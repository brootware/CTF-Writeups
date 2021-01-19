# So Meta

Point: 150

## Category

Forensics

## Question

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png).

## Hint

What does meta mean in the context of files?

Ever heard of metadata?

## Solution

A metadata reading tool is needed to find the flag withtin the image file given. exiftool is one of the many tools available to check the metadat of the image pre-installed with most linux distributions. You can also install it via brew on MacOS.

```bash
brew install exiftool

exiftool pico_img.png | grep picoCTF
Artist                          : picoCTF{SOLUTIONHERE}
```

## Improvement
None
