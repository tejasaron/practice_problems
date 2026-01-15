def max_freq(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    max_count = 0
    result = None

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            result = key

    return result


nums = [1,2,2,3,1,1]

print(max_freq(nums))
