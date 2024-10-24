def xor_string_with_key(input_string, key):
    xor_result = ''.join([chr(ord(char) ^ key) for char in input_string])
    return xor_result

label = "label"

new_string = xor_string_with_key(label, 13)

flag = f"crypto{{{new_string}}}"
print(flag)
