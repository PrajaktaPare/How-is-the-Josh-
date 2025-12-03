l=[1,1,1,2,3,4,4,5]
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)