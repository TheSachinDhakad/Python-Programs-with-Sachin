class A:
    def method1(self):
        print("this a methos from class A")
class B(A):
    def method1(self):
        print("this a methos from class B")
class C(A):
    def method1(self):
        print("this a methos from class C")

class D(C,B):
    def method1(self):
        print("this a methos from class D")
        pass

a = A()
b = B()
c = C()
d = D()
d.method1()