import random
import string

def make_key(alphabet):
    key = list(alphabet)
    random.shuffle(key)
    return key

def make_cipher(text, key, alphabet):
    chars = list(text)
    for i, c in enumerate(text):
        chars[i] = key[alphabet.index(c)]
    return ''.join(chars)