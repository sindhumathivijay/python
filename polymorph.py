"""class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")
class penguin:
    def fly(self):
        print("penquin cant fly")
    def swim(self):
        print("penguin can swim")
def flying_test(bird):
    bird.fly()
    bird.swim()
blu=parrot()
peggy=penguin()
flying_test(blu)
flying_test(peggy)"""""
#inheritance
class parent:
    parentattr=100
    def __init__(self):
        print("calling parent constructor")
    def parentmethod(self):
        print("calling parent method")
    def setattr(self,attr):
        parent.parentattr=attr
    def getattr(self,attr):
        print("parent attribute",parent.parentattr)
class child(parent):
    def __init__(self):
        super().__init__()
        print("calling the child constructor")
    def childmethod(self):
        print("calling child method")
c=child()
c.parentmethod()
c.childmethod()
c.getattr(5)
print(parent.__doc__)