def clumsy_factorial(n):
    stack = []
    stack.append(n)
    for x in range(1,n):
        operation = x % 4
        i=n-x
        if operation == 1:  # Multiplication
            stack[-1] *= i
        elif operation == 2:  # Division
            stack[-1] = int(stack[-1] / i)
        elif operation == 3:  # Addition
            stack.append(+i)
        else:  # Subtraction
            stack.append(-i)            
    return sum(stack)
inputVal = int(input())
outVal = clumsy_factorial(inputVal)
print(outVal)
