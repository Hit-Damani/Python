def average(a, b, c):
    d = int((a+b+c)/3)
    return d

A1 = int(input("Enter the first number  : "))
A2 = int(input("Enter the second number : "))
A3 = int(input("Enter the third number  : "))

result = average(A1, A2, A3)
print(f"\nThe average of the three numbers {A1}, {A2} and {A3} is: {result}")