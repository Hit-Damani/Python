favourite_numbers = [5, 7, 12, 25]
another_favourite_numbers = [1225, 2512]

print(favourite_numbers)
favourite_numbers.append(1225)
print(favourite_numbers)

favourite_numbers.pop()
print(favourite_numbers)

favourite_numbers.extend(another_favourite_numbers)
print(favourite_numbers)


# Some methods of list
my_favourite_places = ["Diu", "Mumbai"]
print(my_favourite_places)

my_favourite_places.append("Surendranagar")
my_favourite_places.append("Ahmedabad")
print(my_favourite_places)

my_favourite_places.insert(1,"Pune")
print(my_favourite_places)

my_favourite_places.remove("Pune")
print(my_favourite_places)

my_favourite_places.pop()
print(my_favourite_places)

my_favourite_places.reverse()
print(my_favourite_places)

my_favourite_places.sort()
print(my_favourite_places)