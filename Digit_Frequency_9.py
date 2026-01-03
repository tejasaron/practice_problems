def countDigit(n,d):
    count = 0
    while n!=0:
        if n % 10 == d:
            count+=1
        n //= 10
    return count

print(countDigit(155552,5))