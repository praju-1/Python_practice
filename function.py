# john = [1200, 3000, 5000, 6000]
# max = [34566, 8990, 4000, 5000]

# def expense(name):
#     total_expense = 0
#     for i in name:
#         total_expense += i
#     print("Total expense  :", total_expense)
# expense(john)
# expense(max)





# total_expense = 0
# for i in john:
#     total_expense += i
# print("Total expense  :", total_expense)


# total_expense = 0
# for i in max:
#     total_expense += i
# print("Total expense  :", total_expense)


# initlization/declaration
# execution
# calling

# def function_name():
#     execution
# function_name()


# def msg():
#     print("Hello world...")
# msg()

# n1 = int(input("Enter a first number : "))
# n2 = int(input("Enter second number : "))

# def addition(a=30, b=90):
#     return a + b
# a = addition()
# print(a)

# n= int(input("Ente a number : "))
# def even_odd(num):
#     """This function returns even and odd number """
#     # num will be divided by 2
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(n)


# def add(*a):
#     # return a
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)

# add(12, 3,2, 2,3, 4, 12, 3,2, 2,3, 4)


# def info(**a):
#     print(a)

# info(a = 10, b= 30, c = 30)

# def hello(*a, **b):
#     print(a)
#     print(b)

# hello(23, 12, 23, 14,46, a=23, name="John")

# lambda single execution

# def add(a, b):
#     print(a+b)
# add(10, 20)

# x = lambda a, b: a+ b
# print(x(10, 45))

t = (1, 2, 3, 4, 5, 6)
num_list = []
for i in t:
    num_list.append(i)
print(num_list)

result = [i**2 for i in t]
print(result)