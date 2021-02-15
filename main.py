def left_difference(a_list, b_list):
    return set(a_list) - set(b_list)


def remove_zero(a_list):
    result = [el for el in a_list if el != 0]
    return result


if __name__ == '__main__':
    # Задача 1
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 5, 6, 7]
    print('Первая задача')
    print(left_difference(a, b))

    # Задача 2
    c = [0, 1, 0, 3, 0, -1, 10, 0]
    print('Вторая задача')
    print(remove_zero(c))
