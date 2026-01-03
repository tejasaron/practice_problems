def isPalindrome(n):
    num1 = n
    rev = 0
    while n != 0:
        rev = (rev + (n % 10)) * 10
        n //= 10
    return num1 == int(rev/10)

print(isPalindrome(123)) 