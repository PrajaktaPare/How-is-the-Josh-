l=[1,2,3,4,5,6,7,8,9]

def sum3(l,target):
    a=[]
    for i in range(len(l)):
        k=target-l[i]
        for j in range(i+1,len(l)):
            m=k-l[j]
            if m in l[j+1:]:
                if l[i]+l[j]+m==target:
                    a.append([l[i],l[j],m])
    return a


print(sum3(l,15))