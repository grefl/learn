import sys

def max_sub_array(array):
    best = current = -sys.maxint 

    for num in nums:
        current = max(-sys.maxint, num + current) 
        best    = max(best, current) 
    return best




print(max_sub_array())

