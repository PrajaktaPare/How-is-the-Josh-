l=[-1,2,-2,4,5,6,7,-6,-5,-9,-7,6,9,8]

def rearrange_pn(l):
    p=[]
    n=[]
    r=[]
    i,j=0,0
    for k in range(len(l)):
        if l[k]>=0:
            p.append(l[k])
        else:n.append(l[k])
    while i<len(p) and j<len(n):
        r.append(p[i])
        r.append(n[j])
        i=i+1
        j=j+1

    return r


print(rearrange_pn(l))