try:
    apples = int(input("Enter the number of apples \n"))
    mx = int(input("Enter the maximun number to cheack \n"))
    mn = int(input("Enter the minimum number to cheack \n"))

except ValueError:
    print("please Enter the interger value ")
    exit()

for i in range (mn,mx+1):
    if apples%i==0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not divisor of {apples}")



        

