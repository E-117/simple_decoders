import binascii
a = input("Enter your hex string:")
for hex_string in a:
    data = bytes.fromhex(a)
print(data)
