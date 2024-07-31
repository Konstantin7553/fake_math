def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second


result1 = divide(15, 3)
print(result1)
result2 = divide(15, 0)
print(result2)