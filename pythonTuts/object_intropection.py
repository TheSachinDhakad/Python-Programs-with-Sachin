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


skillf = Employee("skill","f")
# print(skillf.email)
# print(type(skillf))
# print(id(skillf))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
