def buble_sort(some_list):
    sort = False
    while sort is False:
        sort = True
        for index in range(len(some_list) - 1):
            if some_list[index] > some_list[index + 1]:
                some_list[index], some_list[index + 1] = \
                    some_list[index + 1], some_list[index]
                sort = False
    return some_list


print(buble_sort([9, 2, 6, 4, 9, 2, 6, 4]))
