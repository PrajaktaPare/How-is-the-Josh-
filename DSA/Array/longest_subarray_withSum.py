l=[1,2,3,4,5,6,7,8,9,10]

def longest_substring_kSum(l,s):
    max_len=0
    ss=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            ss+=l[j]
            if ss==s:
                if j-i+1>max_len:
                    max_len=j-i+1
                    
    return max_len

print(longest_substring_kSum(l,6))