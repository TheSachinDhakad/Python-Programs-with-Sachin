# # f = open("simple.txt" , "w")
# f = open("simple.txt" , "a")
# a = f.write("i am currrently study nri grp\n")
# print(a)
# f.close()
f = open("simple.txt" , "r+")
print(f.read())
f.write("thank you!")