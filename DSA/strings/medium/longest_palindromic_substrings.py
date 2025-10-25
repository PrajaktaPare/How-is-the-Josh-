s = "babad"

def longest_palindromic_substring(s):
    ans = ""  # Keep the longest palindrome found
    for i in range(len(s)):
        j = len(s) - 1
        while j >= i:
            if s[i:j+1] == s[i:j+1][::-1]:
                if j - i + 1 > len(ans):
                    ans = s[i:j+1]
                break  # No need to check smaller substrings
            j -= 1
    return ans

print(longest_palindromic_substring(s))
