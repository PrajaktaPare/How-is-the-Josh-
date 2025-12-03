l = ["abc", "abcd", "abcde"]

# Step 1: take the shortest string (prefix can't be longer than this)
prefix = min(l, key=len)

for s in l:
    while not s.startswith(prefix):
        prefix = prefix[:-1]   # reduce prefix one char at a time
        if prefix == "":
            break

print(prefix)
