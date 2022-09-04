yearAge = int(input("What is your age / Year of birth.."))
isAge = False
isYear = False
if len(str(yearAge))==4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("you are the oldest person in alive..")
    exit()

if(isYear>2023):
    print("you are not yer born....")
    exit()

if isAge:
    yearAge = 2023-yearAge

print(f"you will be 100 year old in {yearAge+100}")


a = int(input("Enter the year want to know your age in \n"))

print(f"you will be {a - yearAge} years old in {a}")


