a=[10,20,30,'python','django','html']
print(a)
print(a[:])
print(a[3:])
print(a[:5])
print(a[2:5])
print(a[-3:-1])
a[0]=50
print(a)
print(len(a))
string="python with django framework"
print(list(string))
str1="23 44 44 56 77"
print(list(str1))
a.append("1234")
print(a)
marklist=[90,80,95,85,100]
avg=sum(marklist)/len(marklist)
print(int(avg))
A=[10,20,40,400,-1,0]
print(max(A))
b=[40,60,70]
c=['css','java','script']
print(a+b+c)
details=[('ram',20,25),('john',40,80),('kavin',18,35),('somu',25,40)]
l1=details[0]
l2=details[1]
l3=details[2]
l4=details[3]
l5=l1+l2+l3+l4
print(l5)
L1=[x for x in l5 if type(x)== str]
L1.sort()
print("name in ascending order:",L1)
L1.remove(L1[1])
print(L1)
details.reverse()
print(details)


