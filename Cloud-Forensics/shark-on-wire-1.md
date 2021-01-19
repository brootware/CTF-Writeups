# shark on wire 1

Point: 150

## Category

Forensics

## Question

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.

## Hint

Try using a tool like Wireshark
What are streams?

## Solution

Wireshark is needed to solve this challenge. After some googling from the hints, simply following the UDP streams on wireshark will lead to the flag hidden inside the packet capture.

## Improvement
None
