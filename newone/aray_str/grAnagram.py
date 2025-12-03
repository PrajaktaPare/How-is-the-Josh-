l = ["cat", "ate", "tac", "tea", "eat"]
anagrams = {}

for word in l:
    key = ''.join(sorted(word))   # sort letters to get key
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]

# Get grouped anagrams
rl = list(anagrams.values())
print(rl)
