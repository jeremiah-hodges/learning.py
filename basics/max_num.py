
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:

        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result = max_num(199999, 23332, 2332)
print(result)
