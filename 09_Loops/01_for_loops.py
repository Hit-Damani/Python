a = int(input("Enter a number you want a table for: "))
print("Here's the table of", a, end="\n\n")

for i in range(1 , 11):
    print(a, "X", i , "=", a*i)

print(end="\n")
print("Thank You")   