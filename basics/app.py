
# r is for read only
file = open("employees.txt", "r")

# print(file.readlines())

for employee in file.readlines():
    print(employee)

file.close()

# a is to add to an already existing file

file = open("employees.txt", "a")

file.write("Franco")

file.write("\nKelly")

file.close()

# w can create a new file

file2 = open("employees1.txt", "w")
file2.close()