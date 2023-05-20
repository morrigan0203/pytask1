""" from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)
count = 10
while count > 0:
    count -= 1
    num1 = int(input("Введите число:"))
    if num1 > num:
        print("Искомое число меньше")
    elif num1 < num:
        ("Искомое число меньше")
    elif num1 == num:
        print("Вы угадали")
        break
else:
    print("Начните игру заново! в следующий раз вам обязательно повезет!")    
 """

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)
count = 10
while count > 0:
    count -= 1
    num1 = int(input("Введите число:"))
    if num1 == num:
        print("Вы угадали")
        break
    if num1 > num:
        print("Искомое число меньше")
        continue
    if num1 < num:
        print("Искомое число меньше")
else:
    print("Начните игру заново! в следующий раз вам обязательно повезет!")    

