def to_bin(text):
    for c in text:
        char_in_bin = bin(ord(c))[2:]
        for i in char_in_bin.rjust(8, '0'):
            yield int(i)


def big_text_to_bin(text, block_length=64):
    bits_buffer = []
    for bit in to_bin(text):
        bits_buffer.append(bit)
        if len(bits_buffer) == block_length:
            yield bits_buffer
            bits_buffer = []
    if bits_buffer:
        bits_buffer.extend(list(to_bin(''.join(['.'] * ((block_length - len(bits_buffer)) / 8)))))
        yield bits_buffer


def from_bin(array):
    return unichr(int(''.join(map(str, array)), 2))


def get_text_1():
    return '''My tea's gone cold I'm wondering why I..'''


def get_text():
    return '''My tea's gone cold I'm wondering why I..
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
it's not so bad..'''
