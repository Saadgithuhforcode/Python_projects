def calculator():
    print(' Calculator')
    print(' operations: +, -, *, /')

    num1 = float(input('Enter first number: '))
    operation = input('Enter operation: ')
    num2 = float(input('Enter second number: '))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*': 
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
    else:
        result = " Invalid operation"
    print(f'The result: {result}')

if __name__ == "__main__":
    calculator()