def add(a, b):
    x = b - a
    return x

c = add(1,2)
c1 = add(b = 2, a = 1)
print(c)
print(c1)

def add1(d, e, plus=1):
    y = d + e + plus
    return y

f = add1(1,2)
print(f)

def add2(g, h, plus=0):
    i = g + h + plus
    return i

j = add2(1, 2, 3)
print(j)

