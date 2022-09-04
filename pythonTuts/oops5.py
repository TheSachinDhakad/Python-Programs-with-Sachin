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

        # param = string.split("-")
        # return cls(param[0],param[1],param[2])


sachin = Employee("sachin", "5000", "student")
nitesh = Employee("nitesh", "4000", "student")
karan = Employee.from_str("karan-420-student")
print(karan.salary)

Employee.no_of_leaves = 89
sachin.change_leaves(34)













