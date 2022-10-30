from re import ASCII
from Crypto.Util.number import *
a = input("Enter integers here:")

print(hex(int(a)));
#we get 0x
#remove the 0x
text = bytes.fromhex(a).decode("ASCII")
print(text)