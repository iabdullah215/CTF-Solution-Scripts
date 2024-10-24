from Crypto.Util.number import long_to_bytes

integer_value = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

message = long_to_bytes(integer_value)

message_str = message.decode('utf-8')
print(message_str)
