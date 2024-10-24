import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byte_data = bytes.fromhex(hex_string)

base64_encoded = base64.b64encode(byte_data).decode('utf-8')
print(base64_encoded)
