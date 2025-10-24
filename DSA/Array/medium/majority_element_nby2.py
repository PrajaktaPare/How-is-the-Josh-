l=[1,2,3,4,1,1,1,1]
ll=[2,2,2,2,2,3,4,5]
def majority_element(l):
    n=len(l)
    d={}
    for i in range (n):
        d[l[i]]=d.get(l[i],0)+1
        
    for i,j in d.items():
        if j>n/2:
            return i
print(majority_element(ll))