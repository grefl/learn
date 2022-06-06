import heapq
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

    
def top_k_freq_elements_heap(nums, k):
    m = {}
    for n in nums:
        if n not in m:
            m[n] = 1
        else:
            m[n] +=1
    max_heap = [(-freq, val) for val, freq in m.items()]
    heapq.heapify(max_heap) 
    answer = []
    while len(answer) < k:
        answer.append(heapq.heappop(max_heap)[1])
    return answer

if __name__ == "__main__":
    nums = [4,1,-1,2,-1,2,3] 
    k = 2
    res1 = top_k_frequent_elements(nums, k)
    res2 = top_k_freq_elements_heap(nums, k)
    print(res1)
    print(res2)
   

