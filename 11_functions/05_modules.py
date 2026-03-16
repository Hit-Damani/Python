# Two Types of Modules in Python
# 1. Built-in modules
# 2. External modules
# List of all built in module ---> https://docs.python.org/3/py-modindex.html

import math
import mymodule
import requests
print(math.sqrt(17))

a = input("Enter a name: ")
mymodule.greet(a)

r = requests.get("https://www.google.com")
print(r.text)
print(r.status_code)

url = "https://api.github.com"
response = requests.get(url)
data = response.json()
print(data)
