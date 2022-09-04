class Dad:
    basketball = 1
class Son(Dad):
    dance = 1
    def isdance(self):
        return f"yes i dance {self.dance} no of times "

class Grandsun(Son):

    dance = 6

    def isdance(self):
        return f"yes i dance very awesome {self.dance} no of times "

darry = Dad()
larry = Son()
harry = Grandsun()
print(harry.isdance())
print(harry.basketball)
