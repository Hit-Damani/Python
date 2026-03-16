# declaring a global variable inside a function means that the variable is global and can be accessed anywhere in the program
def sum(a, b):
    global z
    z = 1
    print("Hey I am summing... and the answer is.... ", end = "")
    c = a + b
    return c

def greet():
    global z
    z = 2

z = 7
print(sum(5,7))
greet()
print(z)

# if i am not calling function in which i have declared global variable then it will pick that value of z which is outside the function
