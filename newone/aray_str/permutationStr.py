# def permute(s):
#     res = []
    
#     def backtrack(path, remaining):
#         if not remaining:
#             res.append(path)
#         else:
#             for i in range(len(remaining)):
#                 # choose character at index i
#                 backtrack(path + remaining[i], remaining[:i] + remaining[i+1:])
    
#     backtrack("", s)
#     return res

# # Example
# s = "abc"
# print(permute(s))


from itertools import permutations

s = "abc"
perm = [''.join(p) for p in permutations(s)]
print(perm)
