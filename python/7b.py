class Animal:
 def __init__(self, name, age):
    self.name = name
    self.age = age
 def speak(self):
    print("The animal speaks.")
class Dog(Animal):
 def bark(self):
    print("The dog barks.")
# Creating an object of the Dog class
dog = Dog("Max", 3)
# Demonstrating the speak() method of the Animal class
dog.speak()
# Demonstrating the bark() method of the Dog class
dog.bark()