# Longest increasing subsequence (LIS).

def LIS(arr):
    n = len(arr)
    if n == 0:
        return 0

    # dp[i] = length of LIS ending at index i
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(arr))  # Output: 5 (LIS: 10,22,33,50,60)
