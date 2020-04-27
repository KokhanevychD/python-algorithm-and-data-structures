import random


test_list = list(range(10000))
random.shuffle(test_list)


def QuickSort(some_list):
    temp_list_lt = []
    temp_list_rt = []
    pivot = some_list[0]

    for item in some_list[1:]:
        if item > pivot:
            temp_list_rt.append(item)
        elif item <= pivot:
            temp_list_lt.append(item)
    temp_list_lt.append(pivot)

    if some_list != temp_list_rt + temp_list_lt:
        if len(temp_list_lt) >= 2:
            temp_list_lt = QuickSort(temp_list_lt)
        if len(temp_list_rt) >= 2:
            temp_list_rt = QuickSort(temp_list_rt)
    else:
        return some_list
    some_list = temp_list_lt + temp_list_rt
    return some_list


print(QuickSort(test_list))
