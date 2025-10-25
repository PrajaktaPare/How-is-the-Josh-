l=[1,2,4,1,2,3,4,1,2]

def longest_cons_sequence(l):
    i=0
    r=[]
    finalr=[]
    minlen=0
    while i<len(l):
        r=[l[i]]
        j=i+1
        while j<len(l) and l[j]-l[j-1]==1:
            r.append(l[j])
            j=j+1
            if len(r)>minlen:
                minlen=len(r)
                finalr.extend(r)

            i=j
    return finalr



print(longest_cons_sequence(l))

        