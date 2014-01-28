import random
import string


def makeKey():
    key = list(string.ascii_uppercase)
    random.shuffle(key)
    return key

def makeCipher(text):
    key = makeKey()
    chars = list(text)
    for i, c in enumerate(text):
        chars[i] = key[string.ascii_uppercase.index(c)]
    return ''.join(chars), key