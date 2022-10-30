import binascii
import base64
hex_string = input("Enter your hex string: ");
a = bytes.fromhex(hex_string)

text = base64.b64encode(a)
print(text)
