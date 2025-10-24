a=[12,13,14,15,16,17]

def sec_lar_ele(a):
    max=a[0]
    smax=a[1]

    for i in range(len(a)):
        if a[i]>max:
            smax=max
            max=a[i]
            
    return smax

print(sec_lar_ele(a))