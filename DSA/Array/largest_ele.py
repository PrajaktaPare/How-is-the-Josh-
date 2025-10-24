a=[44,66,33,22,88,92]

def lar_ele(a):
    max=a[0]
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
    return max

print(lar_ele(a))
