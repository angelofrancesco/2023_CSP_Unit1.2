# Write a method called addSubtract()
# This method should take a parameter called operation
# When the method is called, do the operation in
# the parameter to all numbers in the list


def addSubtract(operation):
    num1 = [2, 5, 6, 98, 32, 123]
    num2 = [5, 67, 89, 34, 1, 4]

    index = 0
    # For each loop - Kiedes Style
    for val in num1:
        if operation == 'add':
            print(num1[index] + num2[index])
        else:
            print(num1[index] - num2[index])
        index += 1

# Method calls
addSubtract("add")
addSubtract("subtract")