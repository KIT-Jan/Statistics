import numpy as np
import matplotlib.pyplot as plt

def N_over_n(N, n) -> float:
    """ Return N over n """

    return np.math.factorial(N) \
           /(np.math.factorial(n) * np.math.factorial(N-n))

def binomial(N, n, p, q) -> float:
    """ Returns the probability for exact n occurences """

    return N_over_n(N, n) * p**n * q**(N-n)

p = 0.5 #probability that event occurs
q = 1-p #probability that event does not occur
N = 100 #number of experiments
n = range(N) #number of occurences
#(for which we want to know the probability)
W_list = [binomial(N, n, p, q) for n in range(N)]

if round(np.sum(W_list), 0) != 1.0:
    print("Statistics is broken!")
else:
    plt.bar(n, W_list)
    plt.show()