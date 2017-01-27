from fractions import gcd

import prime

FERMA = [17, 257, 65537]


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def eiler(p, q):
    return (p - 1) * (q - 1)


def generate_keys():
    """Returns (public_key, private_key)."""

    while True:
        p, q = prime.generate_pq(1024, 160)
        n = p * q

        phi = eiler(p, q)
        e = [x for x in FERMA if gcd(x, phi) == 1]

        if len(e) == 0:
            continue
        e = e[0]

        d = extended_gcd(e, phi)[1]
        if d <= 0:
            continue

        return (e, n), (d, n)


def encrypt(data, public_key):
    e, n = public_key
    res = 0
    while data > 0:
        m = data % n
        data //= n

        c = pow(m, e, n)

        res = res * n + c
    return res


def decrypt(data, private_key):
    d, n = private_key
    res = 0
    while data > 0:
        c = data % n
        data //= n

        m = pow(c, d, n)

        res = res * n + m
    return res


def test():
    public_key, private_key = generate_keys()
    data = int('1234567890abcdef' * 2, 16)
    encrypted = encrypt(data, public_key)
    decrypted = decrypt(encrypted, private_key)

    print 'ok' if data == decrypted else 'failed'
    print
    print 'data:\n', hex(data)
    print 'encrypted:\n', hex(encrypted)
    print 'decrypted:\n', hex(decrypted)


if __name__ == '__main__':
    test()
