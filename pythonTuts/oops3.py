class Employee:
    no_od_leaves = 10
    def __init__(self,name , salary , role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetail(self):
        return  f"name is {self.name} salary is {self.salary} and role is {self.role}"


sachin = Employee("sachin" , "5000" , "student")
# sachin.name = "sachin"
# sachin.salary = 500
# sachin.role = "student"
print(sachin.salary)
#
# nitesh = Employee()
# nitesh.name = "sachin"
# nitesh.salary = 500
# nitesh.role = "friend"


# a = sachin.printdetail()
# print(a)
# print(sachin.no_od_leaves)