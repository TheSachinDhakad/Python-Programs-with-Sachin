class Employee:
    no_of_leaves = 9
    def __init__(self , name , salary , role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetial(self):
        return f"the name is {self.name} and salary is {self.salary} amd the role {self.role}"

    @classmethod
    def change_of_leave(cls,leaves):
        cls.no_of_leaves = leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        # return f"the name is {self.name} and salary is {self.salary} amd the role {self.role}"
        return f"Employee('{self.name}' , {self.salary} , '{self.role}')"
    def __str__(self):
        return f"the name is {self.name} and salary is {self.salary} amd the role {self.role}"


emp1 = Employee("sachin" , 450 ,"programmer")
# emp2 = Employee("nitesh" , 150 , "cleaner")
# print(emp1 + emp2)
# print(emp1 / emp2)
print(emp1)
print(repr(emp1))
