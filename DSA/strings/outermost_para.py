s = "((()))"


def outermostPara(s):
    cnt=0
    r=""
    for i in s:
        if i=='(':
            if cnt>0:
                r+=i
            cnt=cnt+1
        else:
            if cnt>0:
                r+=i
            cnt=cnt-1
    return r

print(outermostPara(s))       