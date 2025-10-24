l=[1,2,3,4,5,6,7,8,9]

def two_sum(l,target):
    for i in range(len(l)):
        complement=target-l[i]
        for j in range(i+1,len(l)):
            if l[j]==complement:
                return "yes"
    
    return "no"
        

print(two_sum(l,11))
print(two_sum(l,24))

