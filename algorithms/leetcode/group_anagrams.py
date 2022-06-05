import collections

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


    return True 
# dumb version.
# times out
def group_anagrams(anagrams):
    m = {} 
    i = j =  0
    for i in range(len(anagrams)):
        for j in range(len(anagrams)):
            if (anagrams[i] is not None and anagrams[j] is not None) and valid_anagram(anagrams[i], anagrams[j]):
                if i in m:
                    m[i].append(anagrams[j])
                    anagrams[j] = None
                else:
                    m[i] = [anagrams[j]]
            
    return [d[1] for d in  m.items()]


def group_anagrams2(anagrams):
    m = {} 
    for word in anagrams:
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)
        if sorted_word in m:
            m[sorted_word].append(word)
        else:
            m[sorted_word] = [word]
    return [d[1] for d in m.items()]

def group_anagrams_leetcode(strs):
    ans = {}
    # ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        if tuple(count) not in ans:
            ans[tuple(count)] = [s]
        else:
            ans[tuple(count)].append(s)
    return ans.values()


if __name__ == "__main__":
    
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    strscopy = ["eat","tea","tan","ate","nat","bat"]
    strs2 = ['']
    strs3 = ["",""]
    #res_4 = group_anagrams2(strscopy)
    #res_5 = group_anagrams2(strs2)
    #res_6 = group_anagrams2(strs3)
    #print(res_4)
    #print(res_5)
    #print(res_6)
    print(group_anagrams_leetcode(strs1))

