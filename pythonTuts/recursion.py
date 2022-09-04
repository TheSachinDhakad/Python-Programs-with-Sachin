"""function called itself its called recursion"""
def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def fect_recursive(n):
    if n ==1:
        return 1
    elif n ==0:
        return 1
    else:
        return n * fect_recursive(n-1)

n = int(input("Enter a number : "))
# print(f"the fectorial of {n} is  ",fect_recursive(n))
print(factorial_iterative(n))



