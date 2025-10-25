s = "tree"

def sort_freq(s):
    d={}
 
    for i in range(len(s)):
        d[s[i]]=d.get(s[i],0)+1

    return sorted(d)

print(sort_freq(s))