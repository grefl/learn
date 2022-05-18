


# O(n+m) = O(max(n,m))
def counting_sort(a):
    counter = {}
    maxn = 0
    
    for num in a:
        if num > maxn: maxn = num
        if num in counter:
            counter[num] +=1
        else:
            counter[num] = 1

    for num in a:
        iters = counter[num]
        for i in range(0, iters):
            a[i+num] = num
    for key, num in counter.items():
        print(key, num)
counting_sort([1,2,3,4,4,5,2,1,0, 0, 2, 3, 2])
