s="prajakta"
v="aeiou"
vcnt,ccnt=0,0
for i in s.lower():
    if i in v:
        vcnt+=1
    else:
        ccnt+=1
    
print(vcnt)
print(ccnt)