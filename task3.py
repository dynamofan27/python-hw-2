def sumNum(num):
    while num > 9:
        res = 0
        for i in str(num):
            res += int(i)
        num = res
    return(num)


print(sumNum(38) == 2)
print(sumNum(40) == 4)
print(sumNum(48) == 3)
print(sumNum(2) == 2)
