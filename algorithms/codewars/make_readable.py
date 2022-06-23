


def make_readable(n):
    s = n % 60
    m = n // 60
    h = m // 60
    m = m % 60
    return ':'.join([str(t) if len(str(t)) == 2 else '0' + str(t) for t in [h,m,s]])

print(make_readable(86399))

