def divisibleByTwoAndThree(nums):

    return [x for x in nums if x % 2 == 0 and x % 3 == 0]

nums = [1,2,3,4,6,9,12]

print(divisibleByTwoAndThree(nums))

    
