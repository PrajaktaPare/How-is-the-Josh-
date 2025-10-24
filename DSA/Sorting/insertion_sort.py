l=[5,4,6,3,8,2,9,1]


def ins(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j-1]>l[j]:
                l[j-1],l[j]=l[j],l[j-1]
            
    return l

p=ins(l)
print(p)