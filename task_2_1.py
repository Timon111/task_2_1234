

a = type(15 * 3)
print("15 * 3 is " + str(a))
b = 15 / 3
if isinstance(b, float):
    print("15 / 3 is " + str(type(b)))
c = 15 // 2
if isinstance(c, int):
    print("15 // 2 is " + str(type(c)))
d = type(15 ** 2)
print("15 ** 2 is " + str(d))
