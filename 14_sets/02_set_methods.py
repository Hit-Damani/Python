s = {1, 2, 25, 3, 16, 12}
print(s)

s.add(11)
s.add(12)
print(s)

s.remove(2)
print(s)

# s.remove(1225)  ----> this will give error bcoz 1225 is not present in the set
# if i remove the element which is not present in the set it will give error bcoz it is not there
# so we used discard
# discard will remove if element is present in the set and if not present then it will not give error
s.discard(1225)
print(s)

s.pop()   # This will remove random element from the set
print(s)