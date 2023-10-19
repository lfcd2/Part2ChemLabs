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


main_matrix = gen_matrix(19)
in_phase_pairs = [
    (0, 3), (0, 6), (0, 9), (0, 12), # sp-sp
    (3, 6), (6, 9), (9, 12), (3, 12), # sp-sp
    (0, 5), (0, 8), (0, 11), (0, 14), (9, 2), (9, 7), (9, 13), (12, 1), (12, 4), (12, 10), # sp-p
    (1, 14), (2, 11), (4, 7), (13, 10), # p-p
    (3, 18), (3, 15), (6, 15), (6, 16), (9, 16), (9, 17), (12, 17), (12, 18), # sp-s
    (4, 18), (7, 16), (10, 17), (13, 17) # test
]
main_matrix = assign_pairs(main_matrix, in_phase_pairs, 1)
out_of_phase_pairs = [
    (3, 2), (3, 7), (3, 13), (6, 1), (6, 4), (6, 10), # sp-p
    (1, 8), (2, 5), (7, 10), (4, 13), # p-p
    (4, 15), (7, 15), (10, 16), (13, 18), # test
    # (5, 18), (5, 15), (8, 15), (8, 16), (11, 16), (11, 17), (14, 17), (14, 18) # s-p
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

