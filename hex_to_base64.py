import binascii
import base64
hex_string = input("Enter your hex string: ");
a = bytes.fromhex(hex_string)

b = a;
text = base64.b64encode(b)
print(text)