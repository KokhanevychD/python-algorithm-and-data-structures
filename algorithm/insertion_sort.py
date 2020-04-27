def insertion(arr):
    for index in range(len(arr)):
        if index != 0 and arr[index] < arr[index - 1]:
            for i in range(index, 0, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


if __name__ == "__main__":
    print(insertion([7, 2, 4, 1, 6]))
