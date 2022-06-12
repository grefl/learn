import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    hello = 'hello'
    #if len(s) <= len(hell):
    #    return "NO"
    i = hi = 0 
    while i < len(s) and hi < len(hello):
        if s[i] == hello[hi]:
            hi +=1
        i +=1
    return "YES" if hi == len(hello) else "NO"
        

print(main())
