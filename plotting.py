import numpy
import matplotlib.pyplot as plt

results = [21.3, 21.1, 21.85, 23.0, 23.25, 23.85, 24.75, 24.05, 23.55, 24.75, 25.0, 24.3, 24.75, 24.8, 25.25, 25.3]
x = numpy.arange(5, 21, 1)
plt.xlabel('Sentences')
plt.ylabel('Deciphered letters')
plt.plot(x, results)
plt.show()