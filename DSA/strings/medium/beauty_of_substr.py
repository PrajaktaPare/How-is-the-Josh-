s = "xyx"
 
def beauty_of_substr(s):
    d={}
    result=0
    for i in range(len(s)):
        if i not in d:
            d[s[i]]=d.get(s[i],0)+1

            values=d.values()
            m=max(values)
            mi=min(values)

            result+=(m-mi)

    return result

print(beauty_of_substr(s)) 