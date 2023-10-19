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


main_matrix = gen_matrix(18)
pair_list = [(0, 3), (0, 6), (0, 9), (0, 12), (3, 6), (3, 12), # SP INTERACTIONS
             (3, 15), (6, 9), (6, 15), (9, 12), (9, 15), (12, 15), # SP INTERACTIONS
             #(0, 15), (3, 9), (6, 12),
             (0, 5), (0, 8), (0, 11), (0, 14), # sp - p interactions A
             (9, 2), (9, 7), (9, 13), (9, 17), # D
             (12, 1), (12, 4), (12, 10), (12, 16), # E
             (1, 14), (2, 11), # top
             (4, 7), (10, 13), # side
             (16, 8), (17, 5)] # bottom
main_matrix = assign_pairs(main_matrix, pair_list, 1)
out_of_phase_pairs = [
    (3, 2), (3, 7), (3, 13), (3, 17), # B SP-P
    (6, 1), (6, 4), (6, 10), (6, 16), # C SP-P
    (15, 5), (15, 8), (15, 11), (15, 14), # F SP-P
    (1, 8), (2, 5), # top
    (7, 10), (13, 4), # side
    (16, 14), (17, 11) # bottom
]
main_matrix = assign_pairs(main_matrix, out_of_phase_pairs, -1)


print(main_matrix)
evals, evects = scipy.linalg.eigh(-main_matrix)

evects = np.transpose(evects)
for eigenvalue, eigenvector in zip(evals, evects):
    print(f'α{round(-eigenvalue, 7):+}β')
    new = []
    for i, val in enumerate(eigenvector):
        new.append(val*np.sqrt(12))
   # print(np.round(new, 5))

