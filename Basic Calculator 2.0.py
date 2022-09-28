import math


# Menu


def menu():
    print("Please select an option:\n1. Add\n2. Substract\n3. Multiply\n4. Divide\n5. Power\n6. Square Root\n"
          "7. Factoriel\n8. GCD(Greatest Common Divisor)\n9. LCM(Least Common Multiplier)\n ")


# InputFuncs

def input_Num1():
    x = input("Enter your first number: ")
    return x


def input_Num2():
    y = input("Enter your second Number: ")
    return y


# Basic funcs

def add(x, y):
    return float(x) + float(y)


def substract(x, y):
    return float(x) - float(y)


def multiply(x, y):
    return float(x) * float(y)


def divide(x, y):
    return float(x) / float(y)


def power(x, y):
    return pow(x, y)


def square(x):
    return math.sqrt(float(x))


def factorial(x):
    return math.factorial(int(x))


def GCD(x, y):
    return math.gcd(int(x), int(y))


def LCM(x, y):
    return math.lcm(int(x), int(y))


# print func


def printFunc(x, y, key):
    if key == '1':
        print(x, " + ", y, " = ", add(x, y))

    elif key == '2':
        print(x, " - ", y, " = ", substract(x, y))

    elif key == '3':
        print(x, " * ", y, " = ", multiply(x, y))

    elif key == '4':
        print(x, " / ", y, " = ", divide(x, y))

    elif key == '5':
        print(x, "to the power of ", y, " is ", pow(int(x), int(y)))

    elif key == '6':
        print("The square root of ", x, " is equal to: ", square(x))

    elif key == '7':
        print("The factorial of ", x, " is equal to: ", factorial(x))

    elif key == '8':
        print("The greatest common divisor of ", x, " and ", y, " is equal to: ", GCD(x, y))

    elif key == '9':
        print("The least common multiplier of ", x, " and ", y, "is equal to: ", LCM(x, y))


# the calculator itself
next_calc = True
while next_calc:

    menu()

    command_num = (input("Enter the selected option: "))
    if command_num in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print("Enter the numbers you want to work with: ")

        # all the actions

        if command_num == '1':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        elif command_num == '2':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        elif command_num == '3':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        elif command_num == '4':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        elif command_num == '5':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        elif command_num == '6':
            x = input_Num1()
            y = 0
            printFunc(x, y , command_num)

        elif command_num == '7':
            x = input_Num1()
            printFunc(x, y, command_num)

        elif command_num == '8':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        elif command_num == '9':
            x = input_Num1()
            y = input_Num2()
            printFunc(x, y, command_num)

        next_input = input("Do you want to continue? \n --- yes/no --- \n")
        if next_input == "no":
            break

    else:
        print("Invalid input. Try again!")