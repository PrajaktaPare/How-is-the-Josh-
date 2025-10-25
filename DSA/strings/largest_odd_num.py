# s = "5347"
s="0214638"

def largest_odd_num(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
        
print(largest_odd_num(s))