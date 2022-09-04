n = 0
print("fibonacci series ")

limit = int(input("Enter a number : "))
def ger(limit):
    a,b = 0,1
    while (a<=limit):
        yield  a
        a,b = b,a+b



def fect(n):
    n = int(input("Enter a number you know a fectorial : "))
    print("the fectorial of your number : ")
    sum = 1
    for i in range(n,0,-1):
        sum = sum*i
        yield sum

g = ger(limit)
for i in g:
    print(i)

f = fect(n)
for i in f:
    print(i)