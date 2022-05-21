a = [2,11,30,31,40]

# basic version
def bs(a,l,r,x):
    m = (l+r) // 2
    print(l,m,r)
    if a[m] == x:
        return m
    elif a[m] < x:
        return bs(a,m+1, r,x)
    elif a[m] > x:
        return bs(a,l,m-1,x)
    else:
        return None

print(bs(a, 0, len(a)-1, 11))



a = [2,11,30,31,40]
x = -1 
# gti = greater than or equal to i
def bs_gti(a,x):
    l =  -1 
    r = len(a) 
    while r > l+1: 
        m = (l+r) // 2
        if a[m] >= x:
            r = m
        else:
            l = m
    print(f"what is r{r}")
    return r 


pos = bs_gti(a, x)

if pos != len(a):
    print("elements greater than i!")
    print(a[pos:])

# less than or equal to i

a = [2,11,30,31,40]
x = -1 
# gti = greater than or equal to i
def bs_lei(a,x):
    l =  -1 
    r = len(a) 
    while r > l+1: 
        m = (l+r) // 2
        if a[m] > x:
            r = m
        else:
            l = m
    return l 

pos = bs_lei(a, 1000)

if pos != -1:
    print("elements less than!")
    print(a[:pos])
