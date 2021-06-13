
notValid1 = True
notValid2 = True

while notValid1:
    try:
        num1 = float(input("Enter number 1: "))
        break
    except ValueError:
        print("This input is not a valid number")


while notValid2:
    try:
        num2 = float(input("Enter number 2: "))
        break
    except ValueError:
        print("This input is not a valid number")


op_unsuported = True

while(op_unsuported):
    op = input("Enter operation ")
    op = op.lower()
    if op == "add" or op == "subtract" or op == "multiply" or op == "divide":
        op_unsuported = False
    else:
        print("Sorry " + op + " is not a supported operation, please choose either add, subtract, multiply, or divide")

if op == "add":
    result = num1 + num2

if op == "subtract":
    result = num1 - num2

if op == "multiply":
    result = num1 * num2

if op == "divide":
    if num2 == 0:
        result = "Divide by Zero... Undefined!"
    else:
        result = num1/num2


print("Answer: " + str(result))