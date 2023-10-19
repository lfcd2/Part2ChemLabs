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
in_phase_pairs = [
    (0, 3), (0, 6), (0, 9), (3, 6), (6, 9), # sp-sp
    (0, 5), (0, 8), (0, 11), (6, 2), (6, 4), (6, 10), (9, 1), (9, 7), # sp-p
    (1, 11), (2, 8), (7, 10), # p-p
    (0, 14), (3, 14), (0, 15), (9, 15), (3, 12), (6, 12), (6, 13), (9, 13),  # sp-s
    (9, 17), (3, 16) # sp-s terminal
]
main_matrix = assign_pairs(main_matrix, in_phase_pairs, 1)
out_of_phase_pairs = [
    (3, 1), (3, 7), # sp-p
    (1, 5), (4, 7), # p-p
    (12, 5), (12, 8), (13, 8), (13, 11), # s-p
    (2, 14), (4, 14), (2, 15), (10, 15) # s-p
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

