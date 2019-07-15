a={'name':'python','age':5,'class':1}
print(a.values())
b={"version":'3.7'}
a.update(b)
print(a)
print(a.keys())
for i in a:
    print(i)
print(a.values())
for i in a:
    print(a[i])
a['year']="1990"
print(a)
del a["age"]
print (a)
a['age']="6"
print(a)
a.clear()
print(a)
A={'name':'python','age':5,'class':1}
x=A.items()
print(x)
print(len(A))
X={'name','gender','age','year'}
Y={}
Y=Y.fromkeys(X)
print(Y)
Y=Y.fromkeys(X,"sindhu")
print(Y)