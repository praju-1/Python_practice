
# try:
#     print(a + b)
# except Exception as e:
#     print(e)
# finally:
#     print("This will always execute")

# a = 10
# b = 20
try:
    def swap_no(a,b):
        try:
            print("Number before swap ")
            print("a :", a)
            print("b :", b)
            c = a
            a = b
            b = c
            print("Number After swap ")
            print("a :", a)
            print("b :", b)
        except Exception as e:
            print(e)
    swap_no(10, 20)
except Exception as e:
            print(e)



