def longest_increasing_subarray(arr):
    max_len = 0
    curr_len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            curr_len += 1
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)

    return max_len

# Example
arr = [1, 2, 2, 3, 4, 1, 2, 3, 4, 5]
print(longest_increasing_subarray(arr))  # Output: 5
