l=[0,1,2,0,3,4,0,0,8]
c=0
rl=[]
for i in l:
    if i==0:
        c=c+1
    else:
        rl.append(i)
rl+=[0]*c
print(rl)