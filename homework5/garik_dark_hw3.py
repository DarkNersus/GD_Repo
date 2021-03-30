tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Игорь'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def return_generator():

    for i in range(len(tutors)):
        if i < len(klasses):
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], None


numb = return_generator()
while (numbers := next(numb)) is not None:
    print(numbers)




