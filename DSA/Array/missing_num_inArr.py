a=[1,2,4,5,6]

def missing_num(a):
    for i in range(len(a)):
        if a[i+1]-a[i]!=1:
            j=a[i]+1
            return(j)
        
        

print(missing_num(a))