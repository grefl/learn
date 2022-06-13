

def validPalindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]
    left  = 0
    right = len(s) -1
    while left < right and s[left] == s[right]:
        print(s)
        print(left, right)
        left  += 1
        if left == right:
            return True
        right -= 1
    return left == right
if __name__ == "__main__":
    print(validPalindrome("a"))
