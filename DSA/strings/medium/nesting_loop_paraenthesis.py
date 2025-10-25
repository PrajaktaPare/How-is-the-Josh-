s = "(1+(2*3)+((8)/4))+1"


def nesting_loop(s):
    p=0
    ans=0
    for i in range(len(s)):

        if s[i]=='(':
            p+=1
            ans=max(ans,p)
        elif s[i]==')':
            p=-1
        
        print(ans)

    return
print(nesting_loop(s))