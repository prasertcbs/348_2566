# a=7
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b) # integer division (int(7/3) in excel)
# print(a%b) # remainder (mod(7,3) in Excel)

come = 4
pay = 3
per_head = 100
# pax = 2

for pax in range(1, 16):
    amt=(pax // come) * pay * per_head + (pax % come) * per_head
    print(pax, amt)