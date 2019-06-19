import locale
from my_asm import MOVSX, XOR, ADD, IMUL, SHL

SYS_ENCODING = locale.getpreferredencoding()

name = input("Please enter the name ")
b_name = name.encode(SYS_ENCODING)

EBX = [0, 0, 0, 0]
EAX = [0, 0, 0, 0]

for numb, each_byte in enumerate(b_name, 1):
    MOVSX(EAX, each_byte)
    ECX = [0, 0, 0] + [numb]
    XOR(EAX, ECX)
    ADD(EBX, EAX)

IMUL(EAX, 6)
SHL(EBX, 7)
ADD(EAX, EBX)

answer = "".join([hex(i).replace('0x', '').upper() for i in EAX if hex(i).replace('0x', '') != '0'])
print("serial:", answer)
