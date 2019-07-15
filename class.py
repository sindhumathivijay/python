"""class clname:
    "this is a example"
    def a(self):
        print("hai")
b=clname()
b.a()
class myclass:
    "this is my second class"
    a=10
    def func(self):
        print("hello")
print(myclass.a)
print(myclass.func)
g=myclass()
g.func()
class myclass:
    "this is my second class"
    a=10
    def __init__(self):
        print("i am constructor")
    def func(self):
        f=12
        print("hello")
    def b(self):
        print("hai",myclass.a)
g=myclass()
g.func()
g.b()
class human:
    def __init__(self,a):
        print('wellll',a)
    def sayhello(self,name=None):
        if name is not None:
            print("hello",name)
        else:
            print("hello")
p=human('hai')
p.sayhello()
p.sayhello("sindhu")
class democlass:
    num=101
    def __init__(self,data):
        print("hh")
        self.a=data
    def read_number(self):
        print(self.a)
        print(self.num)
obj=democlass(44)
obj.read_number()
obj1=democlass(66)
obj1.read_number()
class parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        print(self.name,"sings",song)
    def dance(self):
        print(self.name,"is now dancing")
blu=parrot("Blu",10)
blu.sing("happy")
blu.dance()"""""
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        print("constructor")
    def __del__(self):
        class_name=self.__class__.__name__
        print()
        print(class_name,"destroyed")
p=point()
q=p
r=q
print(id(p))
print(id(q))
print(id(r))
del p
del q
del r
