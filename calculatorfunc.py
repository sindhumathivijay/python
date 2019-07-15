a=int(input("enter a:"))
b=int(input("enter b:"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
x=int(input("choose the option 1 or 2 or 3 or 4:"))
if x==1:
    print(a,"+",b,"=",add(a,b))
if x==2:
    print(a,"-",b,"=",sub(a,b))
if x==3:
    print(a,"*",b,"=",mul(a,b))
if x==4:
    print(a,"/",b,"=",div(a,b))


