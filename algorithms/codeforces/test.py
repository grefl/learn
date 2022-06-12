import sys
input = sys.stdin.readline

def test():
    val = int(input())
    if val > 2 and val % 2 == 0:
        return "YES" 
    return "NO" 

if __name__ == "__main__":
    print(test())
