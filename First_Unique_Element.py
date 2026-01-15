def unq_freq(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    unique_count = []
    result = None

    for key in freq:
        if freq[key] == 1:
            unique_count.append(key)
    
    return unique_count[0]

nums = [4,4,1,5,2,1,2,3]

print(unq_freq(nums)) 