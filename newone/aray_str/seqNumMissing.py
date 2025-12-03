l=[1,2,3,4,6]
for i in range(len(l)-1,0,-1):
    if l[i]-l[i-1]!=1:
        print(l[i]-1)
    else:
        continue