l=[1,2,3,-3]

def subarr_sum0(l):
    sc=0
    
    a=[]
    for i in range(len(l)):
        s=0
        for j in range(i,len(l)):
            s+=l[j]
            if s==0 and (j-i+1)>sc:
                sc=j-i+1
                a=l[i:j+1]
    return a 

print(subarr_sum0(l))
