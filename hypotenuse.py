import math
base=int(input("Enter the base:"))
height=int(input("Enter the height:"))
print("the triangle details as follows:")
print("base:",base)
print("height:",height)
#hypotenuse=math.hypot(base,height)
hypotenuse=math.sqrt(base*base+height*height)
print("the hypotenuse is:",hypotenuse)
         
