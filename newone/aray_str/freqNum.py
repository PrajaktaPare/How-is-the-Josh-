nums = [1,2,2,3,3,4,4,4]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.values())
most_freq_nums = [num for num in freq if freq[num] == max_freq]
print(most_freq_nums)
