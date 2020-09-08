def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    print (num1 or num2)

gcd_rem_division(168, 105)
# print(a) # Выведет 21

