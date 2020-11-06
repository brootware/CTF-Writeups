# What's a net cat?

Point: 100

## Category

Forensics

## Question

Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 41120 to get the flag?

## Hint

nc [tutorial](https://linux.die.net/man/1/nc)

## Solution

As given in the hint, linux command nc needs to be used to establish a TCP connection at destination port 41120 to capture the flag. If everything is correct, there will be a response back from the server.

In the below example, an additonal -w flag is put for a connection timeout of 5 seconds after the connection is established.

```console
nc -w 5 jupiter.challenges.picoctf.org 41120
You're on your way to becoming the net cat master
SOLUTIONHERE
```


## Improvement

None