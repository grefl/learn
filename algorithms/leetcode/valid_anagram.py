from collections import Counter

# Dumb version?
def valid_anagram(s, t):
    """

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Example
    -------------------------------------
    Input: s = "anagram", t = "nagaram"
    Output: true
    -------------------------------------
    """

    if len(s) != len(t):
        # can't be an anagram if they're different lengths
        return False 

    m = {} 
    seen = set()
    for c in s:
        seen.add(c)
        if c not in m:
            m[c] = 1
        else:
            m[c] += 1
    for c in t:
        if c not in m:
            return False 
        m[c] -=1
        if m[c] == 0:
            seen.remove(c)


    return len(seen) == 0

def valid_anagram_v2(s, t):
    """

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Example
    -------------------------------------
    Input: s = "anagram", t = "nagaram"
    Output: true
    -------------------------------------
    """

    if len(s) != len(t):
        # can't be an anagram if they're different lengths
        return False 

    m = {} 
    count = len(s) 
    for c in s:
        if c not in m:
            m[c] = 1
        else:
            m[c] += 1
    for c in t:
        if c not in m:
            return False 
        m[c] -=1
        if m[c] < 0:
            return False
        count -=1

    return count == 0
# Classic means the classic leetcode/normal way to answer this question
def valid_anagram_classic(s, t):
    if len(s) != len(t):
        return False
    m1 = {}
    m2 = {}
    for i in range(len(s)):
        m1[s[i]] = 1 + m1.get(s[i], 0)
        m2[t[i]] = 1 + m2.get(t[i], 0)

    for c in s:
        if m1[c] != m2.get(c, 0):
            return False
    return True 

# How you would probably do this in the wild
def valid_anagram_pythonic(s, t):
    return Counter(s) == Counter(t)
# O(1)
s = "nag"
t = "gan"
s[0] = 12

if __name__ == "__main__":
    s = "anagram" 
    t = "nagaram"
    res_1 = valid_anagram(s, t)
    res_2 = valid_anagram_v2(s, t)
    res_3 = valid_anagram_pythonic(s,t)
    res_4 = valid_anagram_classic(s,t)
    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
