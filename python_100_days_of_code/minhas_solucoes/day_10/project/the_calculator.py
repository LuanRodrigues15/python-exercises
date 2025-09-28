def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

result = 0
answer = ""
calculator = True

while calculator:
    if answer == "":
        num1 = float(input("What's the first number?: "))
    else:
        num1 = result

    print(" | ".join(operations.keys()))
    
    operation = input("Pick an operation: ")

    if operation not in operations:
        print("Invalid option")
        continue

    num2 = float(input("What's the next number?: "))

    result = operations[operation](num1, num2)
    if result is None:
        print("Cannot divide by 0")
        continue

    print(f"{num1} {operation} {num2} = {result}")

    answer = input(f"\nType 'y' to continue calculating with {result}, or 'n' to start a new calculation or 's' to Stop: ").lower()
    if answer == "y":
        continue
    elif answer == "n":
        answer = ""
    else:
        calculator = False

print("Closed")