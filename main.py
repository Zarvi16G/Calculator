from art import logo

# Calculator

# Add


def add(n1, n2):
    return n1 + n2

# Substract


def substract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "I can't divide by Zero"


save_result = None

while True:
    print(logo)
    print("Remember just enter numbers and just the operator\n")

    n1 = float(input("Enter your number: \n"))

    if save_result == None:
        n2 = float(input("Enter your second number: \n"))
    else:
        n2 = save_result

    dict_operations = {
        '+': ['Add', add(n1, n2)],
        '-': ['Substract', substract(n1, n2)],
        '*': ['Multiply', multiply(n1, n2)],
        '/': ['Divide', divide(n1, n2)]
    }
    for symbol in dict_operations:
        print(symbol)
    operator = input("Pick an operation from the line above: ")


    if operator in dict_operations:
        print(
            f"{n1} {operator} {n2} = {dict_operations[operator][1]}")
        repeat = input(
            f"If you want: \n Stop: Type 'n' \n Make a new operation: Type 'y' \n Make operation with {dict_operations[operator][1]}: Type 's' \n").lower()
        if repeat == 'n':
            break
        elif repeat == 'y':
            save_result = None
        elif repeat == 's':
            save_result = dict_operations[operator][1]
    else:
        print(f"The {operator} is not correct, try again.")
