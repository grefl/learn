



def maxScore(cardPoints, K):
    curr = best = sum(cardPoints[:K])
    k = K -1
    step = 1 
    while k >= 0:
       curr -= cardPoints[k] 
       k -=1
       curr += cardPoints[-step]
       step +=1
       best = max(best, curr)
    return best




cardPoints = [2,2,2]
k = 2 
res1 = maxScore(cardPoints, k)
print(res1)

k = 0 
curr = 8 

    
