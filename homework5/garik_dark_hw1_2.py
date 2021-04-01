# task 1
def random_num(n):
    for i in range(1, n, 2):
        yield i


numb = random_num(16)
while (numbers := next(numb)) is not None:
    print('my_generator_15')
    print(numbers)

# task 2
#numb = iter(range(1, 16, 2))
