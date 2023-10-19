import numpy as np
import scipy
b2h6_matrix = -np.array([[0, 1, 0, 0, 0, 0],
                         [1, 0, 1, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 1, 0, 1],
                         [0, 0, 0, 0, 1, 0]])


def gen_matrix(n):
    m = np.zeros((n, n))
    return m


def assign_pairs(m, interaction_list, value):
    for x, y in interaction_list:
        m[x, y] = value
        m[y, x] = value
    return m


main_matrix = gen_matrix(12)
pair_list = [(0, 3), (1, 7), (2, 11), (4, 10), (5, 6), (8, 9)]
main_matrix = assign_pairs(main_matrix, pair_list, 1)
pair_list = [(0, 1), (0, 2), (1, 2),
             (3, 4), (3, 5), (4, 5),
             (6, 7), (6, 8), (7, 8),
             (9, 10), (9, 11), (10, 11)]
main_matrix = assign_pairs(main_matrix, pair_list, 0.25)
print(main_matrix)
evals, evects = scipy.linalg.eigh(-main_matrix)
evects = np.transpose(evects)
for eigenvalue, eigenvector in zip(evals, evects):
    print(f'α{round(-eigenvalue, 7):+}β')
    new = []
    for i, val in enumerate(eigenvector):
        new.append(val*np.sqrt(12))
    print(np.round(new, 5))

