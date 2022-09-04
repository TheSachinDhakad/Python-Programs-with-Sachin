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



sachin = Employee("sachin" , "5000" , "student")
nitesh = Employee("nitesh" , "4000" , "student")

Employee.no_of_leaves = 89
sachin.change_leaves(34)

print(sachin.no_of_leaves)
print(nitesh.no_of_leaves)
