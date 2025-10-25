l=[1,1,1,1,1,1,2,3]

def majority_nby3(l):
    d={}
    for i in range(len(l)):
        d[l[i]]=d.get(l[i],0)+1
    for i , j in d.items():
        if d[i]>len(l)/3:
            return i
        
print(majority_nby3(l))