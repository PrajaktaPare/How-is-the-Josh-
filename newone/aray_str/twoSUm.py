l=[1,2,3,4,5,6]

target=7

for i in range(len(l)):
    r=target-l[i]
    for j in range(i+1,len(l)):
        if l[j] == r:
            print(i,j)