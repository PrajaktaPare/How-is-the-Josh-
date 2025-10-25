s = "paper"
t = "title"


def isomorphic_str(s,t):
    if len(s)!=len(t):
        return False
    dic={}
    for i,j in zip(s,t):
        if i in dic:
            if dic[i]!=j:
                return False
        dic[i]=j

    return "".join(dic[c] for c in s ) 

print(isomorphic_str(s,t))