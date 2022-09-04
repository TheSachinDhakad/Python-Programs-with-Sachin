# def function1():
#     print("sachin")
#
# fun2 = function1
# del function1
#
# fun2()

# def funret(num):
#     if num==0:
#         return print
#
#     if num==1:
#         return sum
#
# a = funret(0)
# print(a)

# def executeer(func):
#     func("this")
#
# executeer(print)


def dec1(func1):
    def nowexe():
        print("executing now")
        func1()
        print("executed")
    return nowexe()
@dec1
def who_is_sachin():
    print("sachin is good boy")

# who_is_sachin = dec1(who_is_sachin)
who_is_sachin()