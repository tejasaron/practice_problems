def hasEvenDigit(n):
    judge = False
    while n!=0 :
        dig = n % 10
        if dig % 2 == 0 :
            judge = True
        n = n // 10
    return judge

print(hasEvenDigit(1245))