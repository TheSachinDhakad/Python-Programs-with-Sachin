# # 0 1 1 2 3 5 8 11 .........
# def fib(n):
#     if n == 1:
#         return 0
#     elif n ==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# n = int(input("ente a number : "))
# for i in range(0,n):
#     print(fib(i))
def Fibonacci(number):
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return (Fibonacci(number - 2) + Fibonacci(number - 1))


number = int(input("Enter the Range Number: "))
for n in range(0, number):
    print(Fibonacci(n))