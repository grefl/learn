
def sort(a):
    if len(a) < 2:
        return a
    mid = len(a) // 2
    b = sort(a[:mid])
    c = sort(a[mid:])
    print(b,c)
    return merge(b,c)
def merge(a,b):
    n = len(a)
    m = len(b)
    i = j = k = 0
    c = [None] * (n+m)
    while i < n or j < m:
        if j == m or (i < n and a[i] < b[j]):
            c[k] = a[i]
            k +=1
            i +=1
        else:
            c[k] = b[j]
            k +=1
            j +=1
    return c

if __name__ == "__main__":
    a = [23, 1,34, 2, 3012, 32349, 11, 10, 23123]
    print(sort(a))

