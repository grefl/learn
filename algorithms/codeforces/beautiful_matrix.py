import sys
input = sys.stdin.readlines

def main():
    vals = [line.strip().split(' ') for line in input()]
    for row, line in enumerate(vals, 1):
        if '1' in line:
            col = line.index('1') + 1
            return abs(3-col) + abs(3-row)



if __name__ == "__main__":
    print(main())
