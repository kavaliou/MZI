def mod(x, p):
    while x < 0:
        return p - (-x) % p
    return x % p


def _extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = _extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def mod_inv(x, p):
    d, x, y = _extended_gcd(x, p)
    return x


def _legendre_symbol(a, p):
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls


def mod_sqrt(a, p):
    if _legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    n = 2
    while _legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def el_sum(x1, y1, x2, y2, p, a):
    if x1 == x2 and y1 == y2:
        alpha = (mod((3 * pow(x1, 2, p)) % p + a, p) * mod_inv((2 * y1) % p, p)) % p
    else:
        alpha = (mod(y2 - y1, p) * mod_inv(mod(x2 - x1, p), p)) % p
    x3 = mod(pow(alpha, 2, p) - x1 - x2, p)
    y3 = mod(-y1 + (alpha * mod(x1 - x3, p)) % p, p)
    return x3, y3


def el_mul(k, x, y, p, a):
    k -= 1
    rx, ry = x, y
    while k > 0:
        if k & 1:
            rx, ry = el_sum(rx, ry, x, y, p, a)
        x, y = el_sum(x, y, x, y, p, a)
        k >>= 1
    return rx, ry


def get_y(x, a, b, p):
    return mod_sqrt(x ** 3 + a * x + b, p)
