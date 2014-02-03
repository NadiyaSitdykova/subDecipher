import getopt
import string
import sys
import decipher
import encipher
import random
import re
import nltk

ALPHABET = string.ascii_uppercase
POPULARITY_OF_LETTERS = 'ETAOINSRHLDCUMFGPWYBVKJXZQ'


def gen_sampling(sampling_size):
    corpus = nltk.corpus.brown.sents()[:]
    index = random.randint(0, len(corpus) - 1 - sampling_size)
    sampling = corpus[index: index + sampling_size]
    text = ""
    for l in sampling:
        sent = (filter(lambda x: re.match("[\w]", x), l))
        text += ''.join(sent).upper()

    return re.sub('[^A-Z]', '', text)


def run(sentences_count):
    text = gen_sampling(sentences_count)
    key = encipher.make_key(ALPHABET)
    cipher = encipher.make_cipher(text, key, ALPHABET)
    return text, cipher, decipher.decipher(cipher, key, ALPHABET, POPULARITY_OF_LETTERS)


def compute(sentences_count, iterations_count):
    sum = 0
    for _ in range(1, iterations_count + 1):
        sum += run(sentences_count)[2][0]
    return sum / iterations_count


def compute_statistic(iterations_count):
    results = []
    for sentences_count in range(5, 21):
        res = compute(sentences_count, iterations_count)
        print("mean value of guessed letters is: ", res, " for ", sentences_count, " sentences")
        results.append(res)
    print(results)
    return results

def sample(sentences_count):
    res = run(sentences_count)
    print('text:\n\n', res[0])
    print('\nenciphered text:\n\n', res[1])
    print('\ndeciphered text:\n\n', res[2][1])

myopts, args = getopt.getopt(sys.argv[1:], "l:q:")

for arg, val in myopts:
    if arg == '-l' and val.isdigit():
        compute_statistic(int(val))
    elif arg == '-q' and val.isdigit():
        sample(int(val))
    else:
        print("Illegal {0} argument: {1}".format(arg, val))