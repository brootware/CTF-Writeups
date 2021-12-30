# Git Pro

Point: 67

## Category

General Skills

## Question

TIT4N was playing valorant when I made some.....or some more...okay..maybe a lot commits in this repo. Can you find which commit contains the treasure?
https://github.com/h3llix/noobCTF/

## Solution

Firstly, the git repository is enumerated and discovered that there are tons of commits within the repo.

```bash
git log --oneline > commits.txt
cat commits.txt
d with the previous text
8574173 Well I was bored with the previous text
f4e1f74 Well I was bored with the previous text
5ce8f50 Well I was bored with the previous text
c799b94 Well I was bored with the previous text
c452afa Well I was bored with the previous text
045a7b3 Well I was bored with the previous text
7ce0192 Well I was bored with the previous text
c75aa42 Well I was bored with the previous text
84cbe7e Well I was bored with the previous text
c75fe2c Well I was bored with the previous text
5fb34ef Well I was bored with the previous text
a4454a6 Well I was bored with the previous text
4efe600 Well I was bored with the previous text
86e9a2f Well I was bored with the previous text
b9f8c92 Well I was bored with the previous text
832ebeb Well I was bored with the previous text
5111f93 Well I was bored with the previous text
e2ec8f7 Well I was bored with the previous text
8641e16 Well I was bored with the previous text
6657c60 Well I was bored with the previous text
6ceebe2 Well I was bored with the previous text
f14f6b9 Well I was bored with the previous text
d10e1e9 Well I was bored with the previous text
c4aeb70 Well I was bored with the previous text
8c158f8 Well I was bored with the previous text
a766c46 Well I was bored with the previous text
f06f963 Well I was bored with the previous text
f92fd28 Well I was bored with the previous text
c41d530 Well I was bored with the previous text
a2eb066 Well I was bored with the previous text
6eeb344 Well I was bored with the previous text
d6b1c2f Well I was bored with the previous text
814e556 Well I was bored with the previous text
751ea21 Well I was bored with the previous text
ae4c703 Well I was bored with the previous text
221c529 Well I was bored with the previous text
f57c4c2 Well I was bored with the previous text
3ddd4ad Well I was bored with the previous text
313343d Well I was bored with the previous text
fadcf9e Well I was bored with the previous text
1c5b6cd Well I was bored with the previous text
0293723 Well I was bored with the previous text
d8d4b58 Well I was bored with the previous text
230e417 Well I was bored with the previous text
7e133ad Well I was bored with the previous text
de4544a Well I was bored with the previous text
b1d345d Well I was bored with the previous text
bfb006f Well I was bored with the previous text
006e1ca Well I was bored with the previous text
0b98e02 Well I was bored with the previous text
7cf4a69 Well I was bored with the previous text
60a8693 Well I was bored with the previous text
a987307 Well I was bored with the previous text
25a29d4 Well I was bored with the previous text
6278db3 Well I was bored with the previous text
c715366 Well I was bored with the previous text
53c351b Well I was bored with the previous text
741371e Well I was bored with the previous text
0f1e9c3 Well I was bored with the previous text
ecc075a Well I was bored with the previous text
63d5fe1 Well I was bored with the previous text
3d371b8 Well I was bored with the previous text
9de6969 Well I was bored with the previous text
5a66e80 Well I was bored with the previous text
317bd04 Well I was bored with the previous text
07b7dab Well I was bored with the previous text
7d4a0a1 Well I was bored with the previous text
7c7b32b Well I was bored with the previous text
942e18e Well I was bored with the previous text
3f1ef7b Well I was bored with the previous text
b91c643 Well I was bored with the previous text
b5f0416 Well I was bored with the previous text
f1b1094 Well I was bored with the previous text
de37256 Well I was bored with the previous text
439bf0c Well I was bored with the previous text
cc9adfa Well I was bored with the previous text
57e311b Well I was bored with the previous text
a2982e8 Well I was bored with the previous text
a2b0672 Well I was bored with the previous text
83517b6 Well I was bored with the previous text
e36bb82 Well I was bored with the previous text
21f0c6d Well I was bored with the previous text
fb3fa39 Well I was bored with the previous text
2817653 Well I was bored with the previous text
71637df Well I was bored with the previous text
2ba1031 Well I was bored with the previous text
35d15e8 Well I was bored with the previous text
07f3809 Well I was bored with the previous text
dda7310 Well I was bored with the previous text
09e88dc Well I was bored with the previous text
bd6078a Well I was bored with the previous text
0494872 Well I was bored with the previous text
00382f5 Well I was bored with the previous text
58d3c27 Well I was bored with the previous text
4afc044 Well I was bored with the previous text
a6dce9c Well I was bored with the previous text
cccb210 Well I was bored with the previous text
bbbd6c8 Well I was bored with the previous text
4fb6aa1 Well I was bored with the previous text
6e0e0c8 Well I was bored with the previous text
b8d7687 Well I was bored with the previous text
07af716 Well I was bored with the previous text
a369ee5 Well I was bored with the previous text
10beafa Well I was bored with the previous text
7af011f Well I was bored with the previous text
bc3891b Well I was bored with the previous text
85b8b52 Well I was bored with the previous text
cf3b538 Well I was bored with the previous text
8907788 Well I was bored with the previous text
772cb6b Well I was bored with the previous text
fddaf36 Well I was bored with the previous text
fa10408 Well I was bored with the previous text
f0071a3 Well I was bored with the previous text
776fce9 Well I was bored with the previous text
f63594c Well I was bored with the previous text
a731753 Well I was bored with the previous text
d3d1512 Well I was bored with the previous text
eedb94e Well I was bored with the previous text
82ff768 Well I was bored with the previous text
9f60d80 Well I was bored with the previous text
6280430 Well I was bored with the previous text
0ee7b58 Well I was bored with the previous text
1a019d6 Well I was bored with the previous text
d73e837 Well I was bored with the previous text
1a89c2a Well I was bored with the previous text
c5f3e62 Well I was bored with the previous text
2ce81aa Well I was bored with the previous text
587b38e Well I was bored with the previous text
8d69de4 Well I was bored with the previous text
ef82bf3 Well I was bored with the previous text
f729b98 Well I was bored with the previous text
6e81304 Well I was bored with the previous text
0972d0b Well I was bored with the previous text
8fb61b3 Well I was bored with the previous text
e53cdc5 Well I was bored with the previous text
d5c3b6c Well I was bored with the previous text
250a68f Well I was bored with the previous text
dd910e3 Well I was bored with the previous text
aa0cfc7 Well I was bored with the previous text
bb8aa7e Well I was bored with the previous text
74ac855 Well I was bored with the previous text
8de5da6 Well I was bored with the previous text
de098f5 Well I was bored with the previous text
930750c Well I was bored with the previous text
7d29df3 Well I was bored with the previous text
a8c3a14 Well I was bored with the previous text
99d3a0f Well I was bored with the previous text
1ead075 Well I was bored with the previous text
0754297 Well I was bored with the previous text
e4349df Well I was bored with the previous text
832566c Well I was bored with the previous text
e0515c3 Well I was bored with the previous text
5ad8c85 Well I was bored with the previous text
3a0f5e9 Well I was bored with the previous text
633a01a Well I was bored with the previous text
036b707 Well I was bored with the previous text
bce0255 Well I was bored with the previous text
b011876 Well I was bored with the previous text
3ae9d5b Well I was bored with the previous text
52aecec Well I was bored with the previous text
ad99c96 Well I was bored with the previous text
bf74597 Here it is yes
aa72569 Fooled you for 9th time
f788f72 Fooled you for 8th time
7a5e119 Fooled you for 7th time
858fd8e Fooled you for 6th time
d1e65b0 Fooled you for 5th time
35582e1 Fooled you for 4th time
61f7c2c Fooled you for 3th time
e056ae0 Fooled you for 2th time
1c9e951 Fooled you for 1th time
f040853 Fooled you for 0th time
dedc985 Noob i can fool you
dafe460 Initial Commit
```

After a ton of googling and reading through git documentations. A way to search all git commits for a string was discovered as below but with no luck.
`git log -S flag`

Further researching into this. I have come across an article and found out about `-p` option which shows the diffs within a file. By combining the -S option and -p option all the differences in commits were listed as below and found the flag.

```bash
git log -S flag -p flag.txt
commit f629b8044f284c93aeb689436083bf33bccd4560
Author: Gaurav Genani <h3llix.pvt@gmail.com>
Date:   Wed Mar 17 14:13:02 2021 +0530

    Bored Again

diff --git a/flag.txt b/flag.txt
index 169b50e..e69de29 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +0,0 @@
-flag{REDACTED}
\ No newline at end of file

commit 13ee095f507ba2c9cba54e5af0ab8d5166c21c13
Author: Gaurav Genani <h3llix.pvt@gmail.com>
Date:   Wed Mar 17 14:12:16 2021 +0530

    Bored Again

diff --git a/flag.txt b/flag.txt
index 50b3b26..169b50e 100644
--- a/flag.txt
```

## Improvement

None
