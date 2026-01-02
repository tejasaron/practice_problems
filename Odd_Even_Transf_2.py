def transformArray(nums):
    #return [x*2 for x in nums if x % 2 == 0 ]
    return [x*2 if x % 2 == 0 else x for x in nums]
nums = [1,2,3,4,5,6]

print(transformArray(nums))