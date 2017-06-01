from collections import namedtuple
import numpy as np
"""
Templates for amino acidic residues
"""

AA_info = namedtuple('AA_info', 'coords atom_names bonds bb sc offset')

BDP_info = AA_info(coords=np.array([[-14.69,  10.15, -18.15],
                                    [-15.46,  11.47, -18.33],
                                    [-16.33,  11.35, -19.46],
                                    [-14.45,  12.62, -18.54],
                                    [-15.15,  13.88, -18.62],
                                    [-13.41,  12.66, -17.39],
                                    [-12.36,  13.57, -17.75],
                                    [-12.76,  11.28, -17.17],
                                    [-11.74,  11.28, -16.03],
                                    [-10.58,  11.62, -16.19],
                                    [-12.26,  11.06, -14.85],
                                    [-13.8,  10.27, -17.01],
                                    [-14.09,   9.95, -19.04],
                                    [-16.06,  11.66, -17.43],
                                    [-13.92,  12.44, -19.49],
                                    [-13.9,  12.98, -16.46],
                                    [-12.19,  11.01, -18.07],
                                    [-16.99,  10.64, -19.31],
                                    [-14.59,  14.56, -19.03]]),
                   atom_names=['C1', 'C2', 'O2', 'C3', 'O3', 'C4', 'O4', 'C5',
                               'C6', 'O6A', 'O6B', 'OR', 'H1', 'H2', 'H3',
                               'H4', 'H5', 'H2o', 'H3o'],
                   bb=[],
                   sc=[],
                   bonds=[(0, 1), (0, 11), (0, 12), (1, 2), (1, 3), (1, 13),
                          (2, 17), (3, 4), (3, 5), (3, 14), (4, 18), (5, 6),
                          (5, 7), (5, 15), (7, 8), (7, 11), (7, 16), (8, 9),
                          (8, 10)],
                   offset=19)

NGA_info = AA_info(coords=np.array([[-15.,   5.88, -16.15],
                                    [-15.3,   7.39, -16.33],
                                    [-16.63,   7.71, -15.78],
                                    [-15.24,   7.7, -17.85],
                                    [-15.52,   9.08, -18.1],
                                    [-13.87,   7.26, -18.45],
                                    [-12.73,   7.93, -17.9],
                                    [-13.71,   5.74, -18.23],
                                    [-12.4,   5.17, -18.83],
                                    [-12.36,   3.77, -18.58],
                                    [-17.03,   8.94, -15.35],
                                    [-16.27,   9.85, -15.15],
                                    [-18.54,   9.06, -15.17],
                                    [-13.75,   5.49, -16.79],
                                    [-17.3,   6.97, -15.77],
                                    [-15.8,   5.34, -16.66],
                                    [-14.56,   7.98, -15.81],
                                    [-16.02,   7.14, -18.36],
                                    [-13.91,   7.52, -19.51],
                                    [-14.54,   5.23, -18.71],
                                    [-19.05,   8.97, -16.13],
                                    [-18.78,  10.05, -14.75],
                                    [-18.91,   8.29, -14.49],
                                    [-12.37,   5.36, -19.91],
                                    [-11.52,   5.64, -18.37],
                                    [-12.52,   7.65, -16.98],
                                    [-12.35,   3.64, -17.61]]),
                   atom_names=['C1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4', 'C5',
                               'C6', 'O6', 'C7', 'O7', 'C8', 'OR', 'HN2', 'H1',
                               'H2', 'H3', 'H4', 'H5', 'H81', 'H82', 'H83',
                               'H6R', 'H6S', 'H4o', 'H6o'],
                   bb=[],
                   sc=[],
                   bonds=[(0, 1), (0, 13), (0, 15), (1, 2), (1, 3), (1, 16),
                          (2, 10), (2, 14), (3, 4), (3, 5), (3, 17), (5, 6),
                          (5, 7), (5, 18), (6, 25), (7, 8), (7, 13), (7, 19),
                          (8, 9), (8, 23), (8, 24), (9, 26), (10, 11), (10, 12),
                          (12, 20), (12, 21), (12, 22)],
                   offset=27)


templates_gl = {'B': BDP_info, 'N': NGA_info}

one_to_three_gl = {'B': 'BDP', 'N': 'NGA'}

three_to_one_gl = {val: key for key, val in one_to_three_gl.items()}
