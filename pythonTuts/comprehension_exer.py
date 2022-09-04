n = int(input("Enter how many items to add in your inventory : "))

i = 0
l =[]

while (i<n):
    a = input("Enter the item : ")
    l.append(a)
    i+=1

choice = int(input("press 1 for generating list comprehension \n press 2 for generating set comprehension \n"
                   " press 3 for generating generator comprehension \n"))

if choice==1:
    list = [item for item in l]
    print(list)

elif choice==2:
    set = (item for item in l)
    print(set)

elif choice==3:
    gen = (item for item in l)
    for c in gen:
        print(c)
