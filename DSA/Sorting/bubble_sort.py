l=[5,4,6,3,8,2,9,1]

def bs(l):

    for i in range(len(l)):
        s=True
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
                s=True
        if s is not True:
            break
    return l

print(bs(l))