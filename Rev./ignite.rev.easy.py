# The `flag` array extracted from Ghidra (hexadecimal values)
flag = [
    0xfa, 0xaa, 0x2c, 0x7b, 0x18, 0x89, 0x7d, 0x90, 0xc1, 0x44, 
    0x93, 0xd6, 0xfb, 0x33, 0xe2, 0x5a, 0xcd, 0x82, 0xf2, 0x4e, 
    0xd5, 0xf4, 0x97, 0xd4, 0x4f, 0x0c, 0xe4, 0x05, 0xe4, 0x71, 
    0x3b, 0x95, 0x74, 0xb7, 0x33, 0x7d, 0x41, 0x1e, 0xf0, 0x55, 
    0x8c, 0x6c, 0xe2, 0x73, 0xcd, 0x1b, 0xa1, 0xdb, 0x7d, 0x00
]

# Initialize array for recovered input
input_reversed = [0] * 50

# Reverse the transformation process
for i in range(48 - 1, -1, -1):
    # Reverse the operation: input[i] = flag[i] + ((i + 1) * input[i+1]) mod 256
    input_reversed[i] = (flag[i] + ((i + 1) * input_reversed[i + 1])) % 256

# Convert to printable characters, replacing non-printable ones with '?'
printable_flag = ''.join(chr(x) if 32 <= x <= 126 else '?' for x in input_reversed)

print("Recovered Flag (printable):", printable_flag)

# Optionally show the flag in hex
print("Recovered Flag (hex):", ' '.join(f'{x:02x}' for x in input_reversed))
