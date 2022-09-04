f = open("simple.txt" , "rt")
# content = f.read()
# content = f.read(54)
# print("1",content)
#
# content = f.read(55)
# print("2",content)
# for line in f:
#     print(line,end="")

# content = f.readline()
# print(content ,end="")
# content = f.readline()
# print(content ,end="")
content = f.readlines()
print(content)
f.close()






# with open("sakshii_food.txt") as f:
#      c = f.read()
#      print(c)