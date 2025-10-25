s="prajakta pare"

def reverse_words(s):
    r=""
    for i in s.split():
        
        r+=i[::-1]+" "

    return r

print(reverse_words(s))