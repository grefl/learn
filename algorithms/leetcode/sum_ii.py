


def sum_ii(array, target):
    n = len(array)
    left  = 0
    right = n - 1

    while left < right:

        val = array[left] + array[right]
        if val == target:
            return True 
        elif val > target:
            right -=1
        else:
            left +=1
    return False


print(sum_ii([1,2,3,4,5,21, 26, 31, 33, 36, 40, 41, 44, 50], 60))


