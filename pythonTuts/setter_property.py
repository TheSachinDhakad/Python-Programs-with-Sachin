class Employee:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"



    def explain(self):
        return f"the frist name is {self.fname} last name is {self.lname} "
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return  "Email is not set please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter

    def email(self , string):
        print("setting now.........")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None



sachin = Employee("sachin" , "nagar")
niesh = Employee("nitesh" , "nagar")
# print(sachin.email())
print(sachin.email)
# sachin.fname ="dhakad"
# print(sachin.email())  //show the eror use by the property decorater

# print(sachin.email)
sachin.email = "this.that@gmail.com"
print(sachin.email)
print(sachin.fname)

del sachin.email
print(sachin.email)

sachin.email = "sachin.that@gmail.com"
print(sachin.email)


