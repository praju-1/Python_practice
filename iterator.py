# a = "hello"
# for i in a:
#     print(i)
# next()
# iter()
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# num =  int(input("Enter a range : "))
# def test(n):
#     l =[]
#     for i in range(n):
#         l.append(i)
#     return(l)

# print(test(num))


def test1(n):
    for i in range(n):
        yield i**2

# print(test1(6))

for i in test1(6):
    print(i)