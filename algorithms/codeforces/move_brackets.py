import sys

input = sys.stdin.readlines


def main():
    brackets = [line.strip() for idx, line in enumerate(input()[1:]) if idx % 2 == 1]
    output = []
    for bracket in brackets:
        right = 0
        left  = 0
        i = 0
        count = 0
        while i < len(bracket):
            if bracket[i] == '(':
                left += 1
            elif bracket[i] == ')':
                right +=1
                if left < right:
                    count = max(right - left, count) 
            i +=1
        output.append(str(count))
    return '\n'.join(output)

if __name__ == "__main__":
    print(main())
