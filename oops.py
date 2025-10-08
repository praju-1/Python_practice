
# class classname:
#     def func_name():
#     # execution
#         pass

# a = classname()
# a.func_name()

class Msg:
    def __init__(self, a=100, b=200):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def mult(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)
       
m = Msg(10)
m.add()
# print(m.b)
# m.div()