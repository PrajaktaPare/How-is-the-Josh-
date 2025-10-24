m=[[1,2,3],[4,5,6],[7,8,9]]

def rotate_matrix(m):
    for i in range (len(m)):
        for j in range(i,len(m)):
           m[i][j],m[j][i]=m[j][i],m[i][j]

    for i in range(len(m)):
        m[i].reverse()
    return m

print(rotate_matrix(m))