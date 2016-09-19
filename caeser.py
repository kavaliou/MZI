from pprint import pprint
from random import randint

ALPHABET = [
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
]


ENGLISH_FREQUENCY = {
    'A': 0.08167, 'C': 0.02782, 'B': 0.01492, 'E': 0.12702, 'D': 0.04253, 'G': 0.02015,
    'F': 0.02228, 'I': 0.06966, 'H': 0.06094, 'K': 0.00772, 'J': 0.00153, 'M': 0.02406,
    'L': 0.04025, 'O': 0.07507, 'N': 0.06749, 'Q': 0.00095, 'P': 0.01929, 'S': 0.06327,
    'R': 0.05987, 'U': 0.02758, 'T': 0.09056, 'W': 0.02360, 'V': 0.00978, 'Y': 0.01974,
    'X': 0.00150, 'Z': 0.00074
}


def enc(text, offset):
    new_text = ''
    text = text.replace(' ', '').replace('.', '').replace(',', '') \
        .replace('\'', '').replace('-', '').replace('\n', '') \
        .replace(';', '').replace('?', '') \
        .upper()
    for c in text:
        i = (ALPHABET.index(c) + offset) % len(ALPHABET)
        new_text += ALPHABET[i]
    return new_text


def brute_force_decrypt(text):
    return {i: [enc(text, -i)] for i in xrange(len(ALPHABET))}


def frequency(message):
    return {ch: float(message.count(ch))/len(message) for ch in ALPHABET}


def alphabet_correlation(message_frequency):
    return sum(ENGLISH_FREQUENCY[ch] * message_frequency[ch] for ch in ALPHABET)


def frequency_decrypt_caesar(cipher_text):
    variants = []
    for i in range(25):
        d = enc(cipher_text, -i)
        msg_frequency = frequency(d)
        variants.append((i, alphabet_correlation(msg_frequency)))
    return max(variants, key=lambda x: x[1])


def get_text():
    return '''
    My tea's gone cold I'm wondering why I..
    got out of bed at all
    The morning rain clouds up my window..
    and I can't see at all
    And even if I could it'll all be gray,
    but your picture on my wall
    It reminds me, that it's not so bad,
    it's not so bad..

    My tea's gone cold I'm wondering why I..
    got out of bed at all
    The morning rain clouds up my window..
    and I can't see at all
    And even if I could it'll all be gray,
    but your picture on my wall
    It reminds me, that it's not so bad,
    it's not so bad..

    Dear Slim, I wrote but you still ain't callin
    I left my cell, my pager, and my home phone at the bottom
    I sent two letters back in autumn, you must not-a got 'em
    There probably was a problem at the post office or somethin
    Sometimes I scribble addresses too sloppy when I jot 'em
    but anyways; fuck it, what's been up? Man how's your daughter?
    My girlfriend's pregnant too, I'm bout to be a father
    If I have a daughter, guess what I'ma call her?
    I'ma name her Bonnie
    I read about your Uncle Ronnie too I'm sorry
    I had a friend kill himself over some bitch who didn't want him
    I know you probably hear this everyday, but I'm your biggest fan
    I even got the underground shit that you did with Skam
    I got a room full of your posters and your pictures man
    I like the shit you did with Rawkus too, that shit was fat
    Anyways, I hope you get this man, hit me back,
    just to chat, truly yours, your biggest fan
    This is Stan

    My tea's gone cold I'm wondering why I..
    got out of bed at all
    The morning rain clouds up my window..
    and I can't see at all
    And even if I could it'll all be gray,
    but your picture on my wall
    It reminds me, that it's not so bad,
    it's not so bad..

    Dear Slim, you still ain't called or wrote, I hope you have a chance
    I ain't mad - I just think it's FUCKED UP you don't answer fans
    If you didn't wanna talk to me outside your concert
    you didn't have to, but you coulda signed an autograph for Matthew
    That's my little brother man, he's only six years old
    We waited in the blistering cold for you,
    four hours and you just said, No.
    That's pretty shitty man - you're like his fuckin idol
    He wants to be just like you man, he likes you more than I do
    I ain't that mad though, I just don't like bein lied to
    Remember when we met in Denver - you said if I'd write you
    you would write back - see I'm just like you in a way
    I never knew my father neither;
    he used to always cheat on my mom and beat her
    I can relate to what you're saying in your songs
    so when I have a shitty day, I drift away and put 'em on
    cause I don't really got shit else so that shit helps when I'm depressed
    I even got a tattoo of your name across the chest
    Sometimes I even cut myself to see how much it bleeds
    It's like adrenaline, the pain is such a sudden rush for me
    See everything you say is real, and I respect you cause you tell it
    My girlfriend's jealous cause I talk about you
    But she don't know you like I know you Slim, no one does
    She don't know what it was like for people like us growin up
    You gotta call me man, I'll be the biggest fan you'll ever lose
    Sincerely yours, Stan P.S.
    We should be together too


    My tea's gone cold I'm wondering why I..
    got out of bed at all
    The morning rain clouds up my window..
    and I can't see at all
    And even if I could it'll all be gray,
    but your picture on my wall
    It reminds me, that it's not so bad,
    it's not so bad..
    '''


def get_text_2():
    return 'OKDZRDRSNOHMDUDQFNMMZCZMBDZFZHMHJMNVHZLMNSZENNKRNHMDUDQFNMMZCZMBDZFZHMNNNN'


if __name__ == '__main__':
    text = get_text_2()
    offset = randint(0, 26)
    crypted_text = enc(text, offset)
    result = frequency_decrypt_caesar(crypted_text)
    print enc(crypted_text, -result[0])
