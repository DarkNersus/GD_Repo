'''
Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''
percent = int(input("Введите количество процентов: "))
while percent < 0: #100 < percent or percent < 0:
    percent = int(input("Введите количество процентов: "))

if (percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4) and percent % 100 // 10 != 1:
    print(f'{percent} процента')
elif percent % 10 == 1 and percent % 100 // 10 != 1:
    print(f'{percent} процент')
else:
    print(f'{percent} процентов')

