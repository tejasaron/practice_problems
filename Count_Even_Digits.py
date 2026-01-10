
def list_digit(n):
    li_n = []
    while n!=0:
        li_n.append(n%10)
        n//=10
    return li_n

def count_digit(lis):
    s_count = 0

    for x in lis:
        count = 0
        li_n = list_digit(x)
        for x in li_n:
            if x % 2 == 0:
                count+=1
        if count == len(li_n):
            s_count += 1
    return s_count


nums = [24, 135, 80, 7, 0]
print(count_digit(nums))