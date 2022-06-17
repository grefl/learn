def evalRPN(tokens):

    stack = []
    operators = "+-/*"
    for token in tokens:
        if token in operators:
            if token == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1+op2)
            elif token == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2- op1)
            elif token == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 / op1))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 * op1)
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == "__main__":
    ops = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(ops))
