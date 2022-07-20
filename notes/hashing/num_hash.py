

def bitExtracted(number, k, p):  
    return ( ((1 << k) - 1)  &  (number >> (p-1) ) );

def hash(x):
    x = x*x * 31
    return bitExtracted(x, 2, 3) 
