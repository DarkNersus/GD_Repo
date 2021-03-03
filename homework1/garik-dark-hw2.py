'''
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
'''
numbers = [i**3 for i in range(1, 1000, 2)]
result_sum_numbers = 0

for i in numbers:

    check_number = i
    summa_numbers = 0

    while not (check_number == 0):
        summa_numbers = summa_numbers + check_number % 10
        check_number = check_number // 10

    if summa_numbers % 7 == 0:
        result_sum_numbers = result_sum_numbers + i

print(result_sum_numbers)

result_sum_numbers = 0

for i in numbers:

    check_number = i + 17
    summa_numbers = 0

    while not (check_number == 0):
        summa_numbers = summa_numbers + check_number % 10
        check_number = check_number // 10

    if summa_numbers % 7 == 0:
        result_sum_numbers = result_sum_numbers + i

print(result_sum_numbers)

