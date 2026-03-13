# lambda function are anonymous, inline functions

square = lambda x: x*x
'''
As good as writing 
 def square(x):
    return x*x
'''
a = int(input("Enter a number for square: "))
print(square(a))


sum = lambda a,b: a+b
'''
As good as writing
 def sum(a,b):
   return a+b
'''
b = int(input("Enter  the first number for sum: "))
c = int(input("Enter the second number for sum: "))
print(sum(b,c))


