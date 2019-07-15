x=[1,2,3,4,5,6]
#x=int(input("enter the list"))
def sum(x):
    y=0
    for i in x:
        y+=i
    return y
print(sum(x))