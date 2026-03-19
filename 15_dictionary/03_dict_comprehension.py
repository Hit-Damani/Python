a = int(input("Enter a number you want a table for that: "))
table = {i : a * i for i in range(1, 11)}
print(table)