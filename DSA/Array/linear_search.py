l=[1,2,3,4,5,6,7,8]

def linear_search(l,num):
    f=True
    for i in range(len(l)):
        if l[i]==num:
            print(i)
            f=True
        else :
            f=False
    if f is False:
        print("Not present")
     


linear_search(l,5)  
linear_search(l,55)  