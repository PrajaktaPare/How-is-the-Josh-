def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):  # starting index i.
        for j in range(i, n):  # ending index j.
            # calculate the sum of subarray [i...j].
            subarray_sum = sum(arr[i:j+1])

            # Increase the count if sum == k.
            if subarray_sum == k:
                cnt += 1

    return cnt


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)