x = 50
def showData():
    x = 25
    def showData2():
        global x
        x = 55
    print("before calling showData2 " , x)
    showData2()
    print("after calling showData2 " , x)



showData()
print(x)
