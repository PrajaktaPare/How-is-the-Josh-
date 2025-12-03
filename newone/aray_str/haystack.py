# Implement strstr/indexOf (needle in haystack).

def strstr(haystack, needle):
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0  # empty needle

    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i  # first occurrence
    return -1  # not found

# Example
haystack = "hello"
needle = "ll"
print(strstr(haystack, needle))  # Output: 2

needle = "world"
print(strstr(haystack, needle))  # Output: -1
