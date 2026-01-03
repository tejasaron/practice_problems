def reverseNumber(n):
    rev = 0
    while n != 0:
        rev = (rev + (n % 10)) * 10
        n //= 10
    
    return int(rev / 10)

print( reverseNumber(1234) )