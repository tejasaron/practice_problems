def key_map_generate(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

nums = [1,2,2,3,1,1]

print(key_map_generate(nums))