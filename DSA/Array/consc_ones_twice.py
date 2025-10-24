l=[1,2,2,3,3,4,5,5,6]

def consc_ones_twice(l):
    d={}
    i=0
    while i<len(l)-1 :
        if  l[i]==l[i+1]:
            d[l[i]]=d.get(l[i],0)+1
            i=i+2
        else:
            i=i+1
    return d

print(consc_ones_twice(l))

