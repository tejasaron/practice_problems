def countEvenGreaterThanTen(nums):
    #return len([x for x in nums if x > 10])
    return len([x for x in nums if x > 10 and x % 2 == 0])

nums = [5,12,8,20,7,14]

print(countEvenGreaterThanTen(nums))