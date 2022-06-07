



def is_happy(n):
    """
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    """
    numbers = list(str(n))

    s = set()
    temp = -1 

    while temp != 1 and temp not in s:
        s.add(temp)
        temp = sum([int(number)**2 for number in numbers])
        numbers = list(str(temp))
    return temp if temp == 1 else False


def is_happy_leet(n):
    found = set()

    while n > 1:
        if n in found:
            return False
        temp = 0
        found.add(n)
        while n > 0:
            temp += pow(n % 10, 2)
            n = n // 10
        n = temp
    return n
assert is_happy(19)
assert is_happy_leet(2)

