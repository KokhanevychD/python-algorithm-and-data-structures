def mergeSort(some_list):

    def merge(list_l, list_r):
        result = []
        idx_l, idx_r = 0, 0
        while idx_l < len(list_l) and idx_r < len(list_r):
            if list_l[idx_l] < list_r[idx_r]:
                result.append(list_l[idx_l])
                idx_l += 1
            else:
                result.append(list_r[idx_r])
                idx_r += 1
        while idx_l < len(list_l):
            result.append(list_l[idx_l])
            idx_l += 1
        while idx_r < len(list_r):
            result.append(list_r[idx_r])
            idx_r += 1
        return result

    if len(some_list) < 2:
        return some_list
    else:
        idx_m = len(some_list) // 2
        list_l = mergeSort(some_list[:idx_m])
        list_r = mergeSort(some_list[idx_m:])
        return merge(list_l, list_r)


print(mergeSort([1, 2, 4, 5, 8, 2]))
