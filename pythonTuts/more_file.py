f = open("simple.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.seek(10))
print(f.readline())
# print(f.tell())

f.close()
