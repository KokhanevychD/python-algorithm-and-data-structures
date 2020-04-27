
def eratosthenes(num):
    arr = list(range(2, num + 1))
    for i in arr:
        mult = 2
        while i * mult <= num:
            if i * mult in arr:
                arr.pop(arr.index(i * mult))
            mult += 1
    return arr


print(eratosthenes(100))
