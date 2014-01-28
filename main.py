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

testCount = 20
results = list()
for i in range(12, 13):
    sum = 0
    for j in range(1, testCount + 1):
        text = get_sampling(i)
        cipher, key = encipher.makeCipher(text)
        sum += decipher.decipher(cipher, key)
    results.append(sum / testCount)
    print(i, sum / testCount)
print(results)