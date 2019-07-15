class calc:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        A=self.x+self.y
        print(A)
    def sub(self):
        B=self.x-self.y
        print(B)
class calci(calc):
    def mul(self):
        C=self.x*self.y
        print(C)
    def div(self):
        D=self.x/self.y
        print(D)
obj=calci(10,2)
obj.add()
obj.sub()
obj.mul()
obj.div()
obj1=obj
print(id(obj))
print(id(obj1))
print(id(obj1))

