import sys
input = sys.stdin.readline
def main():
    m, n = [int(num) for num in input().strip().split(' ')]

    if n % 2 == 0:
            return n // 2 * m
    return n // 2 * m + (n % 2 * m // 2)





if __name__ == "__main__":
    print(main())
