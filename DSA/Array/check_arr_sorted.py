a=[1,2,3,4,5]
b=[6,4,9,2,0]

def check_sorted_arr(a):
    for i in range(len(a)):
        if a[i+1]-a[i]==1:
            return True
        else:
            return False
        
    if True:
        print("Sorted")
    elif False:
        print("Not Sorted")
        
print(check_sorted_arr(b))
print(check_sorted_arr(b))