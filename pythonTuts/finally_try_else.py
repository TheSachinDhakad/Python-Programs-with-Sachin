f1 = open("sachin_ex.txt")

try:
    f = open("simple.txt")



except Exception as e:
    print(e)

else:
    print("this will run only except is no running ...")

finally:
    print("run anyway .....")
    f1.close()

print("impotant stuff")
