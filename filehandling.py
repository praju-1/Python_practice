# f = open("abcd1.txt", "x")
# print(f)
# 
# writing into file

# print(f.readlines()[1])
f = open("abc.txt", "r")
print(f.read())
# print(f.read())
print(f.seek(200))
print(f.read())
print(f.tell())
