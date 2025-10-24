l=[5,4,6,3,8,2,9,1]

def ss(l):
    
    for i in range(len(l)):
        min=l[i]
        pos=i
        for j in range(i+1,len(l)):
            if l[j]<min:
                min =l[j]
                pos=j
        temp=l[i]
        l[i]=min
        l[pos]=temp
        

    return l

print(ss(l))