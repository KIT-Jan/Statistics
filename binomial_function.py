#pylint: disable=invalid-name
#pylint: disable=redefined-outer-name

""" The functions represent the definition of the binomial function.
    It is used to evaluate the probability of a certain
    occurence of a binary event.
    An example would be the classic random walk:
    The walk can be in positive (1) or negative (-1) direction
    with respective probabilites p and q.
    Now the question is what is the probability of n positive walks
    for N steps in total?
    An example of the distribution is plotted at the end"""

import numpy as np
import matplotlib.pyplot as plt

def N_over_n(N: int, n: int) -> float:
    """ Return N over n """

    return np.math.factorial(N) \
           /(np.math.factorial(n) * np.math.factorial(N-n))

def binomial(N: int, n: int, p: float, q: float) -> float:
    """ Returns the probability for exact n occurences """

    return N_over_n(N, n) * p**n * q**(N-n)

if __name__ == "__main__":
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
