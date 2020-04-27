from insertion_sort import insertion


def bucket(in_list):
    buckets = [[] for i in range(len(in_list))]

    # search bucket for given number
    for item in in_list:
        place = int(item * len(buckets))
        buckets[place].append(item)

    # sorting
    result = []
    for bucket in buckets:
        # skip empty bucket
        if len(bucket) == 0:
            continue
        # use insertion sort on full buckets
        if len(bucket) > 1:
            for item in insertion(bucket):
                result.append(item)
        # just add buckets with 1 element as it is already sorted
        else:
            result.append(bucket[0])
    return result


print(bucket([0.23, 0.22, 0.1, 0.03, 0.6, 0.87]) == [0.03, 0.1, 0.22, 0.23,
                                                     0.6, 0.87])
