class Pet:
    def __init__(self, pet_type, name):
        self.pet_type = pet_type
        self.name = name
    
    def details(self):
        print("I am pet")

class Cat(Pet):
    def __init__(self, pet_type, name, age):
        super().__init__(pet_type, name)
        self.age = age

    def details(self):
        print("I am from cat")
        print("Age is : ", self.age)
        return super().details()
    

class Dog(Pet):
    def __init__(self, pet_type, name, breed):
        super().__init__(pet_type, name)
        self.breed = breed

    def details(self):
        print("Breed is  : ", self.breed)
        return super().details()
    

c = Cat("CAT", "Kitty", 2)
c.details()

d = Dog("Dog", "Tiger", "German shephard")
d.details()