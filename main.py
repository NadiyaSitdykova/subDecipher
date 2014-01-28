import getopt
import sys
import decipher
import encipher
import random
import re
import nltk


def get_sampling(samplingSize):
    corpus = nltk.corpus.brown.sents()[:]
    index = random.randint(0, len(corpus) - 1 - samplingSize)
    sampling = corpus[index: index + samplingSize]
    text = ""
    for l in sampling:
        sent = (filter(lambda x: re.match("[\w]", x), l))
        text += ''.join(sent).upper()

    return re.sub('[^A-Z]', '', text)

def compute_statistic(iterations_count):
    results = list()
    for i in range(5, 21):
        sum = 0
        for j in range(1, iterations_count + 1):
            text = get_sampling(i)
            cipher, key = encipher.makeCipher(text)
            sum += decipher.decipher(cipher, key)[0]
        results.append(sum / iterations_count)
        print(i, sum / iterations_count)
    print(results)
    return results

def sample(sentences_count):
    text = get_sampling(sentences_count)
    print('text:\n', text)
    cipher, key = encipher.makeCipher(text)
    print('enciphered text:\n', cipher)
    decipheredText = decipher.decipher(cipher, key)[1]
    print('deciphered text:\n', decipheredText)

myopts, args = getopt.getopt(sys.argv[1:],"l:q:")

for o, a in myopts:
    if o == '-l':
        if a.isdigit():
            compute_statistic(int(a))
        else:
            print("Illegal arguments: ", a)
    elif o == '-q':
        if a.isdigit():
            sample(int(a))
        else:
            print("Illegal arguments: ", a)