def pas_tri(numrow):
    t=[]
    for i in range(numrow):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=t[i-1][j-1] + t[i-1][j]
        t.append(row)

    return t

print(pas_tri(4))