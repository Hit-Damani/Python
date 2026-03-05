# strings formatting

template = "Hey {}! you are awesome.. take this ${} bag and go to {}"

a = "Hit" 
b = "10000"
c = "London"

s1 = template.format(a, b, c)
print(s1)

print(f"hey {a}! how are you???... how much money you have in {c} currency?? please give me ${b}")