# git is good

Point: 30

## Category

Forensics
https://ctflearn.com/challenge/104

## Question

The flag used to be there. But then I redacted it. Good Luck. https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc


## Solution

The zip folder contained flag.txt file containing the flag. But it was redacted as per the given challenge. The folder also contained a .git file that contains the version history.

```bash
:~/gitIsGood@master bruceymac% cat flag.txt 
flag{REDACTED}
:~/gitIsGood@master bruceymac% ls -la
total 8
drwxr-xr-x@  4 bruceymac  staff   128 Oct 31  2016 .
drwx------@ 70 bruceymac  staff  2240 Jan 15 13:26 ..
drwxr-xr-x@ 13 bruceymac  staff   416 Jan 15 13:26 .git
-rw-r--r--@  1 bruceymac  staff    15 Oct 31  2016 flag.txt
```

Git's version history can be checked by below command
```bash
git log
```

From the log, previous version can be checked out with the guid using the command
```bash
% git checkout 195dd6
Note: checking out '195dd6'.
```

Afterwards, the flag can be retrived from the flag.txt file with simple cat command.

## Improvement

None