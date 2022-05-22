import math

def multiply(x,y):
    temp = [0] * len(x)
    for i in range(0, len(x)):
        temp[i] = x[i] * y[i]
    return temp
def m_scalar(v, s):
    for i in range(0, len(v)):
        v[i] *= s
    return v



def dot_product(a,b):
    return sum([aa * bb for aa, bb in zip(a,b)])

def norm(a):
    length = sum([i * i for i in a])
    if length > 0:
        length = math.sqrt(length)
        for i in range(0, len(a)):
                a[i] = a[i] / length
    return a


if __name__ == "__main__":

    s   =   3 
    k   =  [ 1 ,  2 ]
    j   =  [ 2 ,  3 ]
    # MULTIPLY 
    temp = multiply(k,j)
    print(temp)
    print(m_scalar(temp, s))

    # NORM
    a = [0, 4, -3]

    print(norm(a))

    k   =  [1, 3, 5, 7, 9, 11]
    j   =  [13,15,17, 19, 21, 23]

    dot = dot_product(k,j)
    print(dot)
