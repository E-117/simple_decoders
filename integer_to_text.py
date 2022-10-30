from re import ASCII
from Crypto.Util.number import *
a = input("Enter integers here:")

print(hex(int(a)));
#we get 0x63727970746f7b336e633064316e365f346c6c5f3768335f7734795f6430776e7d
#remove the 0x
text = bytes.fromhex(a).decode("ASCII")
print(text)