
def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    new_iterable = []
    i = 0
    current = iterable[i]
    new_iterable.append(current)
    while i < len(iterable):
        if iterable[i] != current:
            current = iterable[i]
            new_iterable.append(current)

        i +=1
    return new_iterable

if __name__ == "__main__":
    s = 'AAAABBBCCDAABBB'
    res = unique_in_order(s)
    print(res)
