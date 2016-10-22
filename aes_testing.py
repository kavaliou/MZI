import random

import read_write as rw
import AES


if __name__ == '__main__':
    text = rw.get_text()
    aes = AES.AES([random.randint(0, 255)] * 16)

    encrypted_text = ''
    for i in rw.big_text_to_byte(text):
        encrypted_text += ''.join(map(chr, aes.encrypt(i)))

    decrypted_text = ''
    for i in rw.big_text_to_byte(encrypted_text):
        decrypted_text += ''.join(map(chr, aes.decrypt(i)))

    print encrypted_text
    print '\n=============\n'
    print decrypted_text