import random
import string
import nltk
from six.moves import xrange
from ngram_score import ngram_score

fitness = ngram_score('english_bigrams.txt')

def sub_decipher(text, key, alphabet):
    invkey = [string.ascii_uppercase[(key.index(c))] for c in alphabet]
    ret = ''
    for c in text:
        ret += invkey[ord(c) - ord(alphabet[0])]
    return ret

def next_iteration(text, key, alphabet):
    alphabet_size = len(alphabet)
    iterations_count = 1000
    score = fitness.score(sub_decipher(text, key, alphabet))
    count = 0
    while count < iterations_count:
        a = random.randint(0, alphabet_size - 1)
        b = random.randint(0, alphabet_size - 1)
        child = key[:]
        child[a], child[b] = child[b], child[a]
        current_score = fitness.score(sub_decipher(text, child, alphabet))
        if current_score > score:
            score, key = current_score, child[:]
            count = 0
        count += 1
    return score, key

def decipher(cipher, real_key, alphabet, letters_distribution):
    alphabet_size = len(alphabet)
    freqDist = nltk.FreqDist(cipher)
    freqLetters = list(freqDist)
    for c in letters_distribution:
        if not c in freqDist.keys():
            freqLetters.append(c)

    start_key = [None] * alphabet_size
    for i, c in enumerate(letters_distribution):
        start_key[ord(c) - ord(alphabet[0])] = freqLetters[i]

    maxscore = -99e99
    iterations_count = 15
    coincidences = 0
    for _ in xrange(1, iterations_count + 1):
        score, key = next_iteration(cipher, start_key, alphabet)
        if score > maxscore:
            maxscore, maxkey = score, key[:]
            coincidences = 0
            for j, c in enumerate(real_key):
                if c == maxkey[j]:
                    coincidences += 1
        if coincidences == alphabet_size:
            break
    return coincidences, sub_decipher(cipher, maxkey, alphabet)