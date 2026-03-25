class Animal:            # Parent class         
    location = "Mumbai"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("speaking now...")

a1 = Animal("Lion")  
a1.speak()

class Dog(Animal):       # Child class   
    def speak(self):
        super().speak()  # calling parent class method speak
        print("Woof!")

d1 = Dog("Bruno")
d1.speak()
print(d1.location)
