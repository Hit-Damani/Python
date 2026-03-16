def sum(a, b):
    # a and b are local variables 
    c = a + b
    z = 1 # Z is a local variable and it will be destroyed after this function returns
    print(z)
    return c

z = 8
print(sum(5, 7))
print(z)
