
def exp(base, power):
    num = 1
    for index in range(power):
        num = num * base

    return  num

print(exp(5,3))

def exp3(base, power):
    result = 1
    while power > 0:
        result = base * result
        power -= 1

    return result

print(exp3(5,3))