import random
import hashlib


def is_prime(n):
    k = len(bin(n)) - 2

    if n <= 2 or (n & 1) == 0:
        return False
    if n == 3:
        return True

    s = 0
    t = n - 1
    while (t & 1) == 0:
        s += 1
        t /= 2

    for _ in xrange(k):
        a = random.randint(2, n - 2)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue

        for __ in xrange(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        if x == n - 1:
            continue

        return False

    return True


def H(x):
    return int(hashlib.sha1(str(x)).hexdigest(), base=16)


def generate_pq(L, N):
    b = (L - 1) % N
    n = (L - 1) // N

    while True:
        seed = None
        seed_len = None
        q = None
        while True:
            seed = random.randint(1 << (N - 1), 1 << N)
            seed_len = len(bin(seed)) - 2
            U = H(seed) ^ H((seed + 1) % (1 << seed_len))
            q = U | 1 | (1 << (N - 1))
            if is_prime(q):
                break

        counter = 0
        offset = 2

        while True:
            V = [H((seed + offset + k) % (1 << seed_len)) for k in xrange(n + 1)]
            W = sum(v * (1 << (i * N)) for i, v in enumerate(V[:-1])) + (V[-1] % (2 * b)) * (1 << (n * N))
            X = W + (1 << (L - 1))

            c = X % (2 * q)
            p = X - (c - 1)

            if p >= (1 << (L - 1)):
                if is_prime(p):
                    return p, q

            counter += 1
            offset += n + 1

            if counter >= (1 << 12):
                break


def bits(x):
    return len(bin(x)) - 2


def test():
    p, q = generate_pq(1024, 160)
    print 'p:', p
    print 'q:', q


if __name__ == '__main__':
    test()
