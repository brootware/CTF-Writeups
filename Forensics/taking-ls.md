# Taking LS

Point: 30

## Category

Forensics
https://ctflearn.com/challenge/103

## Question

Just take the Ls. Check out this zip file and I be the flag will remain hidden. https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8


## Solution

Dot files in directories are hidden in linux file system. You can use the below command to view hidden files within the zip file provided in the link.
```bash
ls -la
``` 


## Improvement

None