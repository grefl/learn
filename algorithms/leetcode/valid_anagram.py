

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

if __name__ == "__main__":
    s = "anagram" 
    t = "annnnnn"
    res_1 = valid_anagram(s, t)
    res_2 = valid_anagram_v2(s, t)
    print(res_1)
    print(res_2)
