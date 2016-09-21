import read_write as rw

import des

KEY = '1010101110101010100100001010110111010010010100100101011010001001' \
      '1110101010001110111011101000110100101110101011010001010110101011' \
      '1010011000011101001010101111010100010101111010111010111001011011'


def get_keys():
    key_length = len(KEY)
    return KEY[:key_length / 3], KEY[key_length / 3:2 * key_length / 3], KEY[2 * key_length / 3:]


def encrypt(text, keys):
    for key in keys:
        enc = []
        des_key = des.get_keys(key)
        for block in rw.big_text_to_bin(text):
            encrypted_block = des.encrypt(block, des_key)
            enc.extend(encrypted_block)

        text = []
        for i in xrange(len(enc) / 7):
            text.append(rw.from_bin(enc[i * 7:(i + 1) * 7]))

        text = ''.join(text)

    return text


def decrypt(text, keys):
    for key in keys:
        dec = []
        des_key = des.get_keys(key)
        for block in rw.big_text_to_bin(text):
            decrypted_block = des.decrypt(block, list(reversed(des_key)))
            dec.extend(decrypted_block)

        text = []
        for i in xrange(len(dec) / 7):
            text.append(rw.from_bin(dec[i * 7:(i + 1) * 7]))

        text = ''.join(text)

    return text


if __name__ == '__main__':
    keys = get_keys()

    text = rw.get_text()

    encrypted_text = encrypt(text, keys)
    decrypted_text = decrypt(encrypted_text, list(reversed(keys)))

    print encrypted_text
    print '\n============\n'
    print decrypted_text
