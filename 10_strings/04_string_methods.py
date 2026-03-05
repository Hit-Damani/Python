s = "hit damani"

# s[0] = "N"     ----> you cannot do this 
print(s)
a = len(s)
print(a)
print(s.upper())  
print(s.lower())
print(s.capitalize())
print(s.title(), end="\n\n")

method1 = " hello world "
print(method1.strip())
print(method1.lstrip())
print(method1.rstrip(), end="\n\n")

method2 = "python is fun and fun and fun"
print(method2.find("is"))   # return index of first occurence
print(method2.replace("fun", "awesome"), end="\n\n")

method3 = " apple / banana / cherry"
print(method3.split("/"))
print(",".join(["apple", " banana", " cherry"]), end="\n\n")

method4 = "python123"
method4_1 = " "
print(method4.isalpha())
print(method4.isdigit())
print(method4.isalnum())
print(method4.isspace())
print(method4_1.isspace(), end="\n\n")

print(ord("A"))
print(chr(65))


