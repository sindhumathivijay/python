class divide:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def div(self):
        result=self.x/self.y
        print(result)
obj=divide(8,2)
obj.div()
obj1=obj
print(id(obj))
print(id(obj1))