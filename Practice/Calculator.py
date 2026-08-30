menu_list = "1. Add. \n2. Substract. \n3. Multiply. \n4. Divide. \n0. Exit"
print(menu_list)
function = int(input("Enter the correspondig number of the function- "))

while function != "0":
    break

    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))

    if function == 1:
        sum = firstNumber + secondNumber
        print(f"The answer is- {sum:0.2f}")

    elif function == 2:
        substract = firstNumber - secondNumber
        print(f"The answer is- {substract:0.2f}")

    elif function == 3:
        multiply = firstNumber * secondNumber
        print(f"The answer is- {multiply:0.2f}")

    elif function == 4:
        divide = firstNumber / secondNumber
        print(f"The answer is- {divide:0.2f}")

    else:
        print("There seems to be a mistake.")