

def max_sub_array(array):
    copy = [0] * len(array)
    copy[0] = array[0]
    print(len(array), len(copy))
    max_sum = -1
    i = 1
    while i < len(array):
        max_sum = max(copy[i-1] + array[i], array[i], max_sum)
        # copy[i] = array[i] + 
        i+=1
    return max_sum



def test(numbers):
    copy = [0] * len(numbers)
    i = 1
    max_sum = copy[0]  = numbers[0]
    while i < len(numbers):
        num = numbers[i]
        if copy[i-1] < num:
            print('yo')
            print(num)
            copy[i] = max(num, copy[i-1] + num)
        else:
            copy[i] = copy[i-1] + num
        max_sum = max(max_sum, copy[i])
        i +=1
    return max_sum


numbers = [-100, 3, -1, -1, 7, -7, 10, -100 ]
res = test(numbers)
print(res)
