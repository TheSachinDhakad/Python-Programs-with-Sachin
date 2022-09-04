print("Enter the number of the list one by one \n")
size = int(input("Enter the size of the list\n"))
mylist = []
for i in range(size):
    mylist.append(int(input("Enter list element \n")))

print(f"your list is {mylist}")
# mylist = [43,65,34,67,78,4]

revers1 = mylist[:]
revers1.reverse()
revers2 = mylist[::-1]
print(f"my frist reverse is {mylist} is {revers1}")
print(f"my second reverse is {mylist} is {revers2}\n")


revers3 = mylist[:]
for i in range(len(revers3)//2):
    revers3[i],revers3[len(revers3) -i -1] = revers3[len(revers3) -i -1],revers3[i]

    # print((f"the reversed list at i={i} is {revers3}"))


print(f"my thrid reversed is {mylist} is {revers3}")

if revers1==revers2==revers3:
    print("all three methods gives same result")