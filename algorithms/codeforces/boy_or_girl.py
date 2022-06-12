import sys
input = sys.stdin.readline


def main():
    chars = list(input().strip())
    s = set()
    count = 0
    for c in chars:
        if c not in s:
            s.add(c)
            count +=1
    return "CHAT WITH HER!" if count % 2 == 0 else "IGNORE HIM!"




if __name__ == "__main__":
    print(main())
        
            
