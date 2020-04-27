def lattice_m(num1, num2):
    # creating list from given numbers and reverse them
    num1 = [int(num) for num in str(num1)]
    num1.reverse()
    num2 = [int(num) for num in str(num2)]
    num2.reverse()
    # result list with summary length for easy access
    res_list = [0] * (len(num1) + len(num2))

    # loop in loop for multiplication
    for index_x, num_x in enumerate(num1):
        for index_y, num_y in enumerate(num2):
            index_k = index_x + index_y
            hold = num_x * num_y
            # division
            res_list[index_k + 1] += (res_list[index_k] + hold) // 10
            res_list[index_k] = (res_list[index_k] + hold) % 10

    return int(''.join(map(str, reversed(res_list))))


print(lattice_m(1948, 827))
