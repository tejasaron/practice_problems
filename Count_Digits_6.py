def countOddDigits(n):
    count = 0
    while n != 0:
        if (n % 10) % 2 != 0:
            count += 1
        n //= 10
    return count

print(countOddDigits(123456789))