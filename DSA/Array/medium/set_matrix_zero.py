m=[[1,1,1],[1,0,1],[1,1,1]]
def set_matrix_zero(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]==0:
                makeRow(i)
                makeCol(j)

    make_zero(m)
    return (m)
    

def makeRow(i):
    for j in range(len(m)):
        m[i][j]=-1

def makeCol(j):
    for i in range(len(m)):
        m[i][j]=-1
    

def make_zero(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]==-1:
                m[i][j]=0
    # return m


print(set_matrix_zero(m))