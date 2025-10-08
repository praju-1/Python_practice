import threading
# to create thread
# t1 = Thread(target/function, args )
# t1.start()
# t1.join()

from threading import *

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")

# t1 = Hello()
# t2 = Hi()

# t1.start()
# # t1.join()
# t2.start()
# # t2.join()

# print(threading.active_count())
# print(threading.main_thread())

def delayed():
    print("Hello")

t = threading.Timer(3, delayed)
t.start()