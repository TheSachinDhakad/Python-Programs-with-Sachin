class Employee:
    no_of_leaves  = 8
    pass

harry = Employee()
sachin = Employee()

harry.name = "harry"
harry.salary = 455
harry.role  = "istructer"

sachin.name = "sachin"
sachin.salary = 500
sachin.role = "student"
print(sachin.name)
# print(sachin.no_of_leaves)
print(Employee.no_of_leaves)
# sachin.no_of_leaves = 9

print(harry.salary)
print(sachin.__dict__)
# print(Employee.__dict__)

