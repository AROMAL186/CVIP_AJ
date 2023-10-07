import re

def evaluate_expression(expression):
    # Define the order of operations
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def apply_operator(operands, operator):
        if len(operands) < 2:
            return "Invalid expression"
        right, left = operands.pop(), operands.pop()
        if operator == '+':
            operands.append(left + right)
        elif operator == '-':
            operands.append(left - right)
        elif operator == '*':
            operands.append(left * right)
        elif operator == '/':
            if right == 0:
                return "Division by zero error"
            operands.append(left / right)

    def greater_precedence(op1, op2):
        return operators[op1] > operators[op2]

    expression = re.sub(r'\s+', '', expression)  # Remove whitespace
    numbers = []
    operators = []
    i = 0

    while i < len(expression):
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and expression[j] in '0123456789.':
                j += 1
            numbers.append(float(expression[i:j]))
            i = j
        elif expression[i] in '+-*/^':
            while (operators and operators[-1] in '+-*/^' and
                    greater_precedence(operators[-1], expression[i])):
                apply_operator(numbers, operators[-1])
                if numbers[-1] in ("Invalid expression", "Division by zero error"):
                    return numbers[-1]
                operators.pop()
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(numbers, operators[-1])
                if numbers[-1] in ("Invalid expression", "Division by zero error"):
                    return numbers[-1]
            operators.pop()
            i += 1
        else:
            return "Invalid character in expression"

    while operators:
        apply_operator(numbers, operators[-1])
        if numbers[-1] in ("Invalid expression", "Division by zero error"):
            return numbers[-1]

    if len(numbers) == 1:
        return numbers[0]
    else:
        return "Invalid expression"

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Division by zero error"
    except Exception as e:
        return f"Error: {str(e)}"

# Main calculator loop
while True:
    user_input = input("Enter an arithmetic expression (or 'quit' to exit): ")

    if user_input == "quit":
        break

    result = calculate(user_input)
    print("Result:", result)

