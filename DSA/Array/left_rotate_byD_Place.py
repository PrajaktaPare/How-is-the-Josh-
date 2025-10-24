l=[1,2,3,4,5]


def left_rotate(l,d):
    ll=l[0:d]
    l=l[d:]
        
    l.extend(ll)

    return l

print(left_rotate(l,2))
print(left_rotate(l,3))
