
# Binwalk
Point: 30

## Category

Forensics

## Question

Here is a file with another file hidden inside it. Can you extract it? https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY

## Hint

The hint is given in the title. The tool to use here is binwalk.

## Solution

First the given file is reconned using file and binwalk commands as below.
```console
$ file PurpleThing.jpeg 
PurpleThing.jpeg: PNG image data, 780 x 720, 8-bit/color RGBA, non-interlaced

binwalk PurpleThing.jpeg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 780 x 720, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
153493        0x25795         PNG image, 802 x 118, 8-bit/color RGBA, non-interlaced
```

From here we can observe that a PNG file and a Zlib compressed data embedded in the file.

The embedded files are then extracted using binwalk as below
```console
% binwalk -e PurpleThing.jpeg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 780 x 720, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
153493        0x25795         PNG image, 802 x 118, 8-bit/color RGBA, non-interlaced

% ls
PurpleThing.jpeg            _PurpleThing.jpeg.extracted

% cd _PurpleThing.jpeg.extracted && ll
total 328
-rw-r--r--  1 bruceymac  staff     0B 22 Sep 15:26 29
-rw-r--r--  1 bruceymac  staff   161K 22 Sep 15:26 29.zlib
```

From the files extracted I was not able to achieve much as the result of the decompression of zlib file using cyberchef came out gibberish with binary data.

So an alternative solution after further looking around was to use foremost. Foremost is a very useful open source forensic utility which is able to recover deleted files using the technique called data carving.

After installing foremost, following command is ran to extract the PNG file out.
```console
% foremost -i PurpleThing.jpeg 
foremost: /usr/local/etc/foremost.conf: No such file or directory
Processing: PurpleThing.jpeg
|*|

% cd output/png && ll
total 328
-rw-r--r--  1 bruceymac  staff   150K 22 Sep 15:35 00000000.png
-rw-r--r--@ 1 bruceymac  staff    11K 22 Sep 15:35 00000299.png
```

The flag can be found using an image viewer 

## Improvement
None

