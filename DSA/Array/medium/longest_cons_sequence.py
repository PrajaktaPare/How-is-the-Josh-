l=[1,2,4,1,2,3,4,1,2]

def longest_cons_sequence(l):
    i=0
    r=[]
    finalr=[]
    minlen=0
    while i<len(l):
        j=i+1
        if l[j]-l[i]==1:
            r.append(l[i])
            if len(r)>minlen:
                finalr.extend(r)
    return finalr

print(longest_cons_sequence(l)

        