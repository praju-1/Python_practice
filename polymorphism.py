# print(10 * 3)
# print([1, 2, 3] * 2)
# from random import *

# print(len("Hello"))
# print(len([1, 2,3, "Python"]))

class Cat:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name of the cat is : ", self.name)

c =  Cat("Kitty")

class Dog:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name of the dog is : ", self.name)

d =  Dog("Tiger")

def output(a):
    a.display()

output(c)
output(d)