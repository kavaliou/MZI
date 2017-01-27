k = (0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
     0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
     0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
     0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
     0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
     0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
     0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
     0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2)

MOD = 1 << 32


def int_to_bytes(x):
    r = []
    while x > 0:
        r.append(x & 0xff)
        x >>= 8
    if len(r) == 0:
        r = [0]
    return bytearray(reversed(r))


def bytes_to_int(x):
    r = 0
    for b in x:
        r = (r << 8) + int(b)
    return r


def rotr(x, v, bits=32):
    b = x & ((1 << v) - 1)
    return (x >> v) | (b << (bits - v))


def bits_count(x):
    return len(bin(x)) - 2


def sha256(message):
    H = (0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
         0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19)

    m = bytearray(message)
    L = len(m) * 8

    _k = 0
    while (L + 1 + _k) % 512 != 448:
        _k += 1
    m.extend(int_to_bytes((1 << (_k + 64)) | L))

    for t in xrange(0, len(m), 64):
        a = m[t:t + 64]
        w = [bytes_to_int(a[j:j + 4]) for j in xrange(0, len(a), 4)]

        for i in xrange(16, 64):
            s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w.append((w[i - 16] + s0 + w[i - 7] + s1) % MOD)

        a, b, c, d, e, f, g, h = H

        for i in xrange(64):
            Z0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            Ma = (a & b) ^ (a & c) ^ (b & c)
            t2 = (Z0 + Ma) % MOD
            Z1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            Ch = (e & f) ^ ((~e) & g)
            t1 = (h + Z1 + Ch + k[i] + w[i]) % MOD

            h, g, f, e, d, c, b, a = g, f, e, (d + t1) % MOD, c, b, a, (t1 + t2) % MOD

        H = ((_h + v) % MOD for _h, v in zip(H, (a, b, c, d, e, f, g, h)))

    res = 0
    for _h in H:
        res = (res << 32) + _h

    return res


def test_string(data):
    result = sha256(data)

    print 'data: "{}"'.format(data)
    print 'sha256:', hex(result)
    print '-' * 10


def test():
    test_string('The quick brown fox jumps over the lazy dog')
    test_string('Hello World!')
    test_string('Hello World')


if __name__ == '__main__':
    test()
