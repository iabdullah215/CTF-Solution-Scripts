def fnv_1a_32(data):
    fnv_prime = 0x01000193
    hash_value = 0x811c9dc5
    for byte in data:
        hash_value ^= byte
        hash_value = (hash_value * fnv_prime) % (2 ** 32)
    return hash_value

def rotate(s, rotation):
    return ''.join(chr((ord(c) + rotation) % 256) for c in s)

def check_flag(flag):
    if len(flag) != 26:
        return False
    if not flag.startswith("flag{"):
        return False
    
    nine_digit_part = flag[5:14]
    if not nine_digit_part.isdigit() or len(nine_digit_part) != 9:
        return False
    
    hash_value = fnv_1a_32(nine_digit_part.encode('utf-8'))
    if hash_value != 0xc6d39d4c:
        return False

    last_part = flag[14:26]
    expected_rotated = rotate(last_part, -6)
    if expected_rotated != "_Q3eM3tT1t6}":
        return False

    return True

def brute_force_flag():
    for i in range(100000000, 1000000000):  # Loop through 9-digit numbers
        nine_digit_number = str(i).zfill(9)  # Pad with zeros to ensure 9 digits
        flag_candidate = f"flag{{{nine_digit_number}}}"
        
        if check_flag(flag_candidate):
            return flag_candidate  # Return the valid flag

# Print the flag if found
if __name__ == "__main__":
    flag = brute_force_flag()
    if flag:
        print(f"The flag is: {flag}")
    else:
        print("Flag not found.")
