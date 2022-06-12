import sys
input = sys.stdin.readlines

def main():
    ops = [op.strip() for op in input()[1:]]
    x = 0
    for op in ops:
        if '-' in op:
            x -=1 
        else:
            x +=1
    return x



if __name__ == "__main__":
    print(main())
