num1 = int(input("Enter frist number : "))
num2 = int(input("Enter second number : "))
choice = input("enter your choice : [+ , - , * , / ] ")
if num1 == 55 and num2 == 9 and choice == '+':
    print("77")

elif num1 == 6 and num2 == 5 and choice == "*":
    print("25")

elif num1 == 25 and num2 == 10 and choice == "-":
    print("10")

elif num1 ==67 and num2 == 6 and choice == "/":
    print("4")


elif choice == "+":
    print(num1+num2)

elif choice == "-":
    print(num1 - num2)

elif choice == "*":
    print(num1*num2)

elif choice == "/":
    print(num1/num2)

else:
    print("invaid choice")





