# a = input("what is your name")
# b = input("how much you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 stopping the program")
# if a.isnumeric():
#     raise Exception("number are not allowed")
#
# print(f"Hello {a}")

c = input("Enter your name ")
try:
    print(a)

except Exception as e:
    if c == "sachin":
        raise ValueError("sachin is blocked")

    print("variable is not defined..")