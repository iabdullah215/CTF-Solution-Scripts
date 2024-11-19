from pwn import remote
import binascii

conn = remote('3.142.89.90', 31471)

known_plaintext = "00000000000000000000000000000000"
conn.sendlineafter("your message (hex)> ", known_plaintext)

known_ciphertext = conn.recvline().strip().decode()
print(f"Known ciphertext: {known_ciphertext}")

conn.recvline()
flag_ciphertext = conn.recvline().strip().decode()
print(f"Flag ciphertext: {flag_ciphertext}")

known_ciphertext_bytes = binascii.unhexlify(known_ciphertext)

flag_ciphertext_bytes = binascii.unhexlify(flag_ciphertext)

recovered_flag = b""
for i in range(0, len(flag_ciphertext_bytes), 16):
    flag_block = flag_ciphertext_bytes[i:i+16]
    recovered_block = bytes([a ^ b for a, b in zip(known_ciphertext_bytes, flag_block)])
    recovered_flag += recovered_block

print(f"Recovered full flag: {recovered_flag.decode(errors='ignore')}")
