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

class player:
    no_of_game = 4
    def __init__(self , name , game):
        self.name = name
        self.game = game

    def printdetail(self):
        return f"the name is {self.name} and game is {self.game}"

class coolprogrammer(player,Employee):
    pass







sachin = Employee("sachin", "5000", "student")
nitesh = Employee("nitesh", "4000", "student")

shubham = player("shubham" , ["cricket"])
karan = coolprogrammer("karan" , "cricket")
det = karan.printdetail()
print(det)