import sys
input = sys.stdin.readlines

def main():
    params, heights = [[int(num) for num in vals.strip().split(' ')] for vals in input()]
    _, fence_height = params

    min_width = 0
    for height in heights:
        if height > fence_height:
            min_width +=2
        else:
            min_width +=1

    return min_width

if __name__ == "__main__":
    print(main())
