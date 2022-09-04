class A:
    classrav1 = "i am class variable in class A"

    def __init__(self):
        self.var1 = "i am inside class A's constructor"
        self.classrav1 = "instance variable in class A"
        self.special = "i am special veriable"

class B(A):
    classrav1 = "i am in class B"

    def __init__(self):
        # super().__init__()     //call for this B class constructor called

        self.var1 = "i am inside class B's constructor "
        self.classrav1 = "instance variable in class B"
        super().__init__()
        print(super().classrav1)




a = A()
b = B()
print(b.classrav1 , b.var1)
print(b.special)