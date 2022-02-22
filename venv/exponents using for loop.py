def exp_power(base,power):
    result = 1
    for index in range(power):

        result = result * base
    return result
print(exp_power(4, 2))