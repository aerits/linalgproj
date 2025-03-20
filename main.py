import numpy as np
import random as r

markov = np.array([
    #a     b    c    d    e    f
    [0,    3/8, 1/9, 0  , 0  , 0], #a
    [0.75, 0,   2/9, 0  , 3/6, 0], #b
    [0.25, 2/8, 0  , 4/5, 2/6, 0], #c
    [0,    0,   4/9, 0  , 0  , 1/2], #d
    [0,    3/8, 2/9, 0  , 0  , 1/2], #e
    [0,    0,   0  , 1/5, 1/6, 0], #f
])

vec = np.array('1;0;0;0;0;0')

def follow_markov(markov, vector: np.array) -> np.matrix:
    new_vec = markov * vector;
    rand = r.random()
    total_prob = 0;
    index = 0;
    for j in new_vec:
        index += 1;
        for i in j:
            total_prob += i;
            if total_prob >= rand:
                arr = np.array([0, 0, 0, 0, 0, 0])
                arr[index-1] = 1
                return arr.T

def main():
    vec = np.matrix('1;0;0;0;0;0')
    while True:
        vec = follow_markov(markov, vec)
        print(vec)


if __name__ == "__main__":
    main()
