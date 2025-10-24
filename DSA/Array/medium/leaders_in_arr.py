l=[4,7,1,0]

def leaders_in_arr(l):
    r=[]
    i=0
  
    while i<len(l):
        j=i+1
        leader=True
        while j<len(l):
            if l[j]>l[i]:
                leader=False
                break
            j=j+1
        if leader:
            r.append(l[i])
        i=i+1
    return r

print(leaders_in_arr(l))