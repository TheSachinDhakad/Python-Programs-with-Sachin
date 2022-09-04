import pickle
# cars = ["bmw" , "audi" , "maruti" ,"fortuner"]
# file = "mycar.pkl"
# fileobj = open(file , 'wb')
# pickle.dump(cars , fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file , "rb")
mycar = pickle.load((fileobj))
print(mycar)
print(type(mycar))



# tadk   ----> pickle.loads











