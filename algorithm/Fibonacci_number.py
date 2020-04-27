def Fibonacci(num, fibo_list=[]):
    if len(fibo_list) < 1:
        fibo_list.append(0)
        fibo_list.append(1)
    elif fibo_list[-2] + fibo_list[-1] > num:
        return fibo_list
    fibo_list.append(fibo_list[-1] + fibo_list[-2])
    fibo_list = Fibonacci(num, fibo_list)
    return fibo_list


print(Fibonacci(215543))
