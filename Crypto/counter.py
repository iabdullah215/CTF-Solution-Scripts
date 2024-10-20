from Crypto.Util.number import long_to_bytes

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def get_flag(known_guess: str, encrypted_quote_hex: str, encrypted_flag_hex: str):
    encrypted_quote = bytes.fromhex(encrypted_quote_hex)
    encrypted_flag = bytes.fromhex(encrypted_flag_hex)
    guess_bytes = known_guess.encode()
    keystream_guess = xor_bytes(guess_bytes, encrypted_quote[:len(guess_bytes)])
    decrypted_flag_guess = xor_bytes(encrypted_flag[:len(keystream_guess)], keystream_guess)
    return decrypted_flag_guess.decode(errors='ignore')

encrypted_quote_hex = "5667c3646a39e6bf6b1d098aadd003671854a7eab5ceaa3ad1ba21a9754cded388dc883114f7b1ee9aafb360c2d7ca48e8974903636a3f39b623784e344404bd8c29e178d08b033534848bf408e55f8292586f"
encrypted_flag_hex = "4f04e4700925b8a9141b1e87a3d2446c5f62f8b99eccf163d38272a96b7198e9d8e8883242e29dfeb2a1"

original_quote = "I do not believe in taking the right decision, I take a decision and make it right."
flag = get_flag(original_quote, encrypted_quote_hex, encrypted_flag_hex)
print(flag)
