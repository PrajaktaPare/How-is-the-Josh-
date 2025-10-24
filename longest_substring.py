def longest_palindrome(s):
    res = ""
    res_len = 0

    def expand_around_center(l, r):
        nonlocal res, res_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res_len = r - l + 1
                res = s[l : r + 1]
            l -= 1
            r += 1

    for i in range(len(s)):
        expand_around_center(i, i)  # Odd length
        expand_around_center(i, i + 1)  # Even length
    return res


s="aabba"
print(longest_palindrome(s))
# Time: O(n²)
# Space: O(1)
