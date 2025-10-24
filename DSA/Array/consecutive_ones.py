l=[1,2,1,1,3,1,1,1,4]

def consecutive_ones(l):
        max=0
        count=0
        for i in l:
            if i==1:
                count=count+1
                if count>max:
                    max=count
            else:
                count=0
        return max

print(consecutive_ones(l))
                