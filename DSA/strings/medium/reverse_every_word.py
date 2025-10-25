s="prajakta pare"

def reverse_every_Word(s):
    ss=s.split(" ")
    ans=ss[::-1]
    print(ans)
    return " ".join(ans)


print(reverse_every_Word(s))