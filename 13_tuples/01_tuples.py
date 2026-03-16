# tuples are ordered but immutable 

a = (1, 2, 3, 4, 5)
print(a)
# a[2] = 10  this will throw an error bcoz tuples are immutable so we cannot change the value of tuple

b = (1, )  # comma is necessary to create a tuple with single element bcoz parantheses are used to create group things together
print(b)
