# def longest_substring(s):
#     seen = set()
#     left = 0
#     max_len = 0

#     for right in range(len(s)):
#         # If character already in window → shrink window
#         while s[right] in seen:
#             seen.remove(s[left])
#             left += 1

#         # Add current char
#         seen.add(s[right])

#         # Update longest length
#         max_len = max(max_len, right - left + 1)

#     return max_len

# print(longest_substring("abcabcbb"))  # Output: 3


def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0
    start_index = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        # Update longest substring data
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            start_index = left

    return s[start_index : start_index + max_len]

print(longest_substring("abcabcbb"))  
