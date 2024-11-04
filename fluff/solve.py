#the print file function
0x00000000004006a3 : pop rdi ; ret
#after pop add the address of string, then call print_file
0x0000000000400620 <+9>:     call   0x400510 <print_file@plt>

#how to write and where to write flag

0x0000000000400628 <+0>:     xlat   BYTE PTR ds:[rbx]
0x0000000000400629 <+1>:     ret    
0x000000000040062a <+2>:     pop    rdx
0x000000000040062b <+3>:     pop    rcx
0x000000000040062c <+4>:     add    rcx,0x3ef2
0x0000000000400633 <+11>:    bextr  rbx,rcx,rdx
0x0000000000400638 <+16>:    ret    
0x0000000000400639 <+17>:    stos   BYTE PTR es:[rdi],al
0x000000000040063a <+18>:    ret    
0x000000000040063b <+19>:    nop    DWORD PTR [rax+rax*1+0x0]

#no strings available

