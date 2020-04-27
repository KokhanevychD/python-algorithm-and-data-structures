
def stein_gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        if num1 == 0 and num2 == 0:
            return 0
        elif num1 == 0:
            return num2
        return num1

    elif num1 == num2:
        return num1

    elif num1 % 2 == 0 or num2 % 2 == 0:
        if num1 % 2 == 0 and num2 % 2 == 0:
            return 2 * stein_gcd(num1/2, num2/2)
        elif num1 % 2 == 0:
            return stein_gcd(num1/2, num2)
        elif num2 % 2 == 0:
            return stein_gcd(num1, num2/2)

    elif num1 % 2 != 0 and num2 % 2 != 0:
        if num1 > num2:
            return stein_gcd((num1-num2)/2, num2)
        else:
            return stein_gcd((num2-num1)/2, num1)


print(stein_gcd(34, 17))
