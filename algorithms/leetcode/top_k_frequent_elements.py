def take_2nd(el):
    return el[1]
def top_k_frequent_elements(nums, k):
    """
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    """

    s = set()
    m = {}
    for n in nums:
        s.add(n)
        if n not in m:
            m[n] = 1
        else:
            m[n] +=1
    answer = [] 

    for n in s:
        answer.append((n, m[n]))
    return [v for (v, k) in sorted(answer, key=take_2nd, reverse=True)][:k]

    



if __name__ == "__main__":
    nums = [4,1,-1,2,-1,2,3] 
    k = 2
    res = top_k_frequent_elements(nums, k)
    print(res)
   

