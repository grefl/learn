


def sum_ii(array, target):
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.
    """
    n = len(array)
    left  = 0
    right = n - 1

    while left < right:

        val = array[left] + array[right]
        if val == target:
            return [left +1, right+1] 
        elif val > target:
            right -=1
        else:
            left +=1
    return [-1, -1] 


print(sum_ii([1,2,3,4,5,21, 26, 31, 33, 36, 40, 41, 44, 50], 60))


