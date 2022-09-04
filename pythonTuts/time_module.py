import time
initial = time.time()
print(initial)
k = 0
while(k<45):
    print("this is sachin")
    # time.sleep(2)
    k +=1
print("while loop run is ",time.time()-initial)

initial2 = time.time()

for i in range (45):
    print("this is sachin" )
print("for loop run is ",time.time()-initial2)


# l = time.asctime(time.localtime(time.time()))
# print(l)

