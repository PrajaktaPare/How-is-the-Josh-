# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagram")
else:
    d = {}

    for ch in s1:
        d[ch] = d.get(ch, 0) + 1

    for ch in s2:
        if ch not in d or d[ch] == 0:
            print("Not Anagram")
            break
        d[ch] -= 1
    else:
        print("Anagram")
