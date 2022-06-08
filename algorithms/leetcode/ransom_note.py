

def canConstructPython(ransomNote, magazine):
    for letter in ransomNote:
        if letter not in magazine:
            return False
        i = magazine.index(letter)
        magazine = magazine[:i:] + magazine[i+1:]

    return True
def canConstruct(ransomNote, magazine):
    m = {}


    for letter in magazine:
        if letter in m:
            m[letter] +=1
        else:
            m[letter] = 1
    for letter in ransomNote:
        if letter not in magazine:
            return False
        m[letter] -=1
        if m[letter] < 0:
            return False
    return True


def canConstructLeet(ransomNote, magazine):
    chars = [0] * 26 
    for c in magazine:
        chars[ord(c) - ord('a')] +=1
    for c in ransomNote:
        chars[ord(c) - ord('a')] -= 1
        if chars[ord(c) - ord('a')] < 0:
            return False
    return True

if __name__ == "__main__":
    print(canConstruct("aa", "ab"))
    print(canConstructPython("aa", "aab"))
    print(canConstructLeet("aa", "aab"))


