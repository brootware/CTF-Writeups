# Crack-the-hash

https://tryhackme.com/room/crackthehash

## Category

Cryptogrpahy

## Question

Cracking hashes challenges

## Solution workflow

The method of attack used in this solution is called *Dictionary Attack*. (a method of breaking into a password-protected computer or server by systematically entering every word in a dictionary as a password).

Tools used
```
hash-identifier
https://www.tunnelsup.com/hash-analyzer/

hashcat
rockyou.txt
```

First the hashes are identified using hash-identifier to narrow down on the possible hash type used with either ```hash-identifer``` or an online hash-analyzer.

Following is the example workflow of task 1.1.
```bash
┌──(kali㉿kali)-[~/Documents/hashCatList]
└─$ hash-identifier 48bb6e862e54f2a795ffc4e541caed4d
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

Least Possible Hashs:
[+] RAdmin v2.x

```

It is quite helpful to check the hashcat manual to deal with different types of hashes with different IDs included within the tool. In this case, 0 for MD5.
```bash
──(kali㉿kali)-[~/Documents/hashCatList]
└─$ hashcat --help | grep MD5 
      0 | MD5                                              | Raw Hash
   5100 | Half MD5                                         | Raw Hash
     50 | HMAC-MD5 (key = $pass)                           | Raw Hash, Authenticated
     60 | HMAC-MD5 (key = $salt)                           | Raw Hash, Authenticated
  11900 | PBKDF2-HMAC-MD5                                  | Generic KDF

```
Afterwards, hashcat is used together with a list of known hashes based on rockyou.txt.

```bash
┌──(kali㉿kali)-[~/Documents/hashCatList]
└─$ hashcat -m 0 48bb6e862e54f2a795ffc4e541caed4d rockyou.txt
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 1.2 pocl 1.5, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz, 1407/1471 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.                                                                                            
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 65 MB

Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

48bb6e862e54f2a795ffc4e541caed4d:easy # The cracked password is displayed together with the hash here.            
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: 48bb6e862e54f2a795ffc4e541caed4d
Time.Started.....: Tue Jan 19 00:12:54 2021 (0 secs)
Time.Estimated...: Tue Jan 19 00:12:54 2021 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   987.0 kH/s (0.31ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 176128/14344385 (1.23%)
Rejected.........: 0/176128 (0.00%)
Restore.Point....: 172032/14344385 (1.20%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: florida69 -> 311331

Started: Tue Jan 19 00:12:38 2021
Stopped: Tue Jan 19 00:12:56 2021

```

All of the tasks have similar workflow of cracking the hashes. Task 1.4, 2.3 would take quite some time for hashcat to go through all the possible combinations within rockyou.txt database.

## Improvement
None
