# l=[1,2,3,4,0,0,1,1,34,0,5,6,7]

l = [-5, -2, -9]
def kadanes_algo(l):
    sum=float('-inf')
    ll=[]
    for i in range(len(l)):
        s=0
        for j in range(i,len(l)):
            s=s+l[j]
            if s>sum:
                sum=s
                ll=l[i:j+1] 

    print(ll)
    return sum

print(kadanes_algo(l))