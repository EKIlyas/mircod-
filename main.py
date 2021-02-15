def left_difference(a_list, b_list):
    return set(a_list) - set(b_list)


if __name__ == '__main__':
    # Задача 1
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 5, 6, 7]
    print(left_difference(a, b))
