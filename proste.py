min_limit = 1
max_limit = 100000
num = int(input("Введите число от 1 до 100000:         "))
if num < min_limit or num > max_limit:
    print("Неправильное число") 
else:
    for i in range(2, num):
        if  num % i == 0:
            print("Это число составное")
            break
    else:
        print("Это число простое")

    