# i = 0
# while(True):
#     if i <5:
#         i = i+1
#         continue
#     print(i+1 , end=" ")
#     if(i == 44):
#         break
#     i = i+1
#
#
while(True):
    inp = int(input("Enter a number : \n"))
    if inp>100:
        print("congrets you enter a number greater then 100 ")
        break
    else:
        print('TRY AGAIN\n')
        continue