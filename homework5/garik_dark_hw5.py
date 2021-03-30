src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def the_lists(src):

    result = []

    for i in range(len(src)):
        for n in range(len(src)):
            if n != i and src[i] == src[n]:
                break
            elif n == len(src)-1:
                result.append(src[i])

    return result


print(the_lists(src))
