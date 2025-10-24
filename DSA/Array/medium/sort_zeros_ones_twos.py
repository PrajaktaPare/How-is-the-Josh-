l=[1,1,2,0,2,1,0,2]

# def sort_one_two(l):
#     i=0
#     while i>len(l):
#         if l[i]>l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
#             i=i+1

#     return l

# print(sort_one_two(l))



def sort_one_two(l):
    low=0
    mid=0
    high=len(l)-1

    while mid<=high:
        if l[mid]==0:
            l[low],l[mid]=l[mid],l[low]
            mid=mid+1
            low=low+1

        elif l[mid]==1:
            mid=mid+1

        else:
            l[mid],l[high]=l[high],l[mid]
            high=high-1
    return l

print(sort_one_two(l))
