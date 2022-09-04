class Employee:
    no_of_leaves = 8
    def __init__(self,name , salary , role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetail(self):
        return  f"name is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printmathod(string):
        print("this is good " + string)

class programmer(Employee):
    def __init__(self,name , salary , role,language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

    def print_prog(self):
        return f" programmer name is {self.name} salary is {self.salary} and role is {self.role} and " \
               f"the language as {self.language}"






sachin = Employee("sachin", "5000", "student")
nitesh = Employee("nitesh", "4000", "student")

shubham  = programmer("shubham" , "50000" , "programmer" , ["python"])
karan = programmer("karam" , "7000" , "programmer" , ["python","cpp"])
print(karan.print_prog())