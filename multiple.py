class Father:
    def __init__(self, eyes, hairs):
        self.eyes = eyes
        self.hairs = hairs

    def display(self):
        print("Eyes of father is : ", self.eyes)
        print("hair type of father is : ", self.hairs)


class Mother:
    def __init__(self, height):
        self.height = height
    
    def display(self):
        print("Height is  : ", self.height)


class Son(Father, Mother):
    def __init__(self, eyes, hairs, height, talent):
        Father.__init__(self, eyes, hairs)
        Mother.__init__(self,height)
        self.talent = talent

    def display(self):
        Father.display(self)
        Mother.display(self)
        print("IQ of son is  : ", self.talent)

s= Son("Brown", "curly", "tall", 240)
s.display()