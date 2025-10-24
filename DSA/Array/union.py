a=[1,2,3,4]
b=[3,4,5,6]

def union(a,b):
    c=set(a).union(set(b))
    return list(c)

print(union(a,b))