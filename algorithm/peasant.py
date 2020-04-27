def peasant_mult(num1, num2, result=0):
    if num1 <= 0:
        return result
    if num1 % 2 != 0:
        result += num2
    num2 += num2
    result = peasant_mult(num1 // 2, num2, result)
    return result

print(peasant_mult(1948, 827))
