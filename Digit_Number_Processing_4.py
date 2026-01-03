def sumOfDigits(n):
    sum = 0
    while n != 0 :
        sum = sum + (n % 10)
        print(sum)
        n = n // 10
        print(n)
    return sum

print(sumOfDigits(1234))