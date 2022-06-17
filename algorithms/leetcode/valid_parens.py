

def isValid(string):
    m = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = []
    for c in string:
        if c in m:
            stack.append(m[c])
        elif len(stack):
            closing = stack.pop()
            if closing != c:
                return False
        else:
            return False
    return len(stack) == 0 



if __name__ == "__main__":
    string = "()"
    print(isValid(string))

