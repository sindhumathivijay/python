x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[2,4,5],
   [7,8,9],
   [11,1,2]]
n=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        n[i][j]=x[i][j]+y[i][j]
for z in n:
    print(z)