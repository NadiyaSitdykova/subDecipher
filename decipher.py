import random
import string
import nltk
from ngram_score import ngram_score

POPULARITY_OF_LETTERS = 'ETAOINSRHLDCUMFGPWYBVKJXZQ'

fitness = ngram_score('english_bigrams.txt')

def sub_decipher(text, key):
    invkey = [string.ascii_uppercase[(key.index(c))] for c in string.ascii_uppercase]
    ret = ''
    for c in text:
        ret += invkey[ord(c) - ord('A')]
    return ret

def next_iteration(text, key):
    score = fitness.score(sub_decipher(text, key))
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = key[:]
        child[a], child[b] = child[b], child[a]
        current_score = fitness.score(sub_decipher(text, child))
        if current_score > score:
            score, key = current_score, child[:]
            count = 0
        count += 1
    return score, key

def decipher(cipher, real_key):
    freqDist = nltk.FreqDist(cipher)
    freqLetters = list(freqDist)
    for c in POPULARITY_OF_LETTERS:
        if not c in freqDist.keys():
            freqLetters.append(c)

    start_key = [None] * 26
    for i, c in enumerate(POPULARITY_OF_LETTERS):
        start_key[ord(c) - ord('A')] = freqLetters[i]

    i = 0
    maxscore = -99e99
    coincidences = 0
    while i < 15 and coincidences < 26:
        i += 1
        score, key = next_iteration(cipher, start_key)
        if score > maxscore:
            maxscore, maxkey = score, key[:]
            coincidences = 0
            for j, c in enumerate(real_key):
                if c == maxkey[j]:
                    coincidences += 1
    return coincidences