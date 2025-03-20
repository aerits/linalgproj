import numpy as np
import random as r

markov = np.matrix([
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
    rand = r.random() - 0.05
    total_prob = 0;
    indices_with_prob = []
    for i in range(0,6):
        # print(new_vec[i,0])
        if new_vec[i,0] > 0:
            indices_with_prob.append((i, new_vec[i,0]))
    last_index = 0
    for (index, prob) in indices_with_prob:
        # print("total prob" + str(total_prob) + " rand" + str(rand))
        total_prob+=prob;
        if total_prob >= rand:
            arr = np.matrix([[0], [0], [0], [0], [0], [0]])
            arr[index] = [1];
            # print("returning")
            return arr;

        

def main():
    print(markov)
    vec = np.matrix([[1], [0], [0], [0], [0], [0]])
    probability = np.matrix([[0], [0], [0], [0], [0], [0]])
    for i in range(0,1_000_000):
        vec = follow_markov(markov, vec)
        # print(vec.T)
        probability = vec + probability
        # print(vec)
    total = probability.sum()
    probability = probability / total;
    print(probability)
    vec = np.matrix([[1], [0], [0], [0], [0], [0]])
    print(markov**10000 * vec)


if __name__ == "__main__":
    main()
