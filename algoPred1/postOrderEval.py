from collections import deque

example = [8,2,5,"*","+",1,3,2,"*","+",4,"-","/"]

stack = deque()

for unit in example:
    if type(unit) == int:
        stack.append(unit)
    else:
        operandTwo = stack.pop()
        operandOne = stack.pop()
        operator = unit
        match operator:
            case "+":
                stack.append(operandOne + operandTwo)
            case "-":
                stack.append(operandOne - operandTwo)
            case "*":
                stack.append(operandOne * operandTwo)
            case "/":
                stack.append(operandOne / operandTwo)

print(stack)
    




