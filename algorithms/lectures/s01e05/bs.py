
# basic version
def bs(a,l,r,x):
    m = (l+r) // 2
    if a[m] == x:
        return m
    elif a[m] < x:
        return bs(a,m+1, r,x)
    elif a[m] > x:
        return bs(a,l,m-1,x)
    else:
        return None

def faster_than_bs(x):
    """The point is that if you need to search for 1 element
    then you should just be using a hashmap since it's O(1).
    However, binary search gets more useful if you need to get
    values that are greater than or less than x. Then it makes
    more sense to use a binary search function"""
    s = {0:0, 1:1, 2:2, 3:3}
    return s[x]


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
    return r 



# less than or equal to i
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


def faster_than_bs(x):
    s = {0:0, 1:1, 2:2, 3:3}
    return s[x]
if __name__ == "__main__":

    # =============================================
    #       Basic Binary search O(lgn) 
    # =============================================

    a = [2,11,30,31,40]
    print(bs(a, 0, len(a)-1, 11))
    # =============================================
    #       Faster than binary search O(1) 
    # =============================================
    print("hashmap")
    print(faster_than_bs(2))
    # =============================================
    #       Greater than or equal O(lgn) 
    # =============================================
    a = [2,11,30,31,40]
    x = -1 
    pos = bs_gti(a, x)

    if pos != len(a):
        print("elements greater than i!")
        print(a[pos:])

    # =============================================
    #              less than or equal O(lgn)
    # =============================================
    a = [2,11,30,31,40]
    x = -1 

    pos = bs_lei(a, 1000)

    if pos != -1:
        print("elements less than!")
        print(a[:pos])
