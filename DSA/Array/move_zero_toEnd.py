l=[0,1,0,2,3,4,0,5]

def move_to_end(l):
    nl=[]
    for i in range(len(l)):
        if l[i]!=0:
            nl.append(l[i])
    cnt=len(l)-len(nl)        
    nl.extend([0]*cnt)
    return nl

print(move_to_end(l))