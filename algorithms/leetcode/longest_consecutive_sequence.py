
def longest_consecutive_sequence(numbers):
    if len(numbers) == 0:
        return 0
    s = set()
    for num in numbers:
       s.add(num)

    max_sequence = 1 
    for num in s:
        max_copy = 1
        if num -1 in s:
            continue
        num +=1
        while True:
            if num in s:
                max_copy +=1
                num +=1
            else:
                max_sequence = max(max_copy, max_sequence)
                break

    return max_sequence 

print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))
            
            
