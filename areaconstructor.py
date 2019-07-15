import math
class area:
    def __init__(self,r):
        self.r=r
    def circle(self):
        result=math.pi*self.r**2
        print(result)
obj=area(4)
obj.circle()