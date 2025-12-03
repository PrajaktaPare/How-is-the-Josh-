l=[11,12,99,88,55,66,77,44,30,78,89]

sl=0
fl=0

for i in l:
    if i>fl:
        sl=fl
        fl=i
    elif i<fl and i>sl:
        sl=i
print(sl)