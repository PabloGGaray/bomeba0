import numpy as np
from numpy.testing import assert_almost_equal
import filecmp
from ..biomolecules import Glycan

gc = Glycan('pdbs/2LIQ_min.pdb', linkages=[4, -3])


def test_exclusions():
    # this test is valid for 2LIQ
    reference = {(60, 69), (54, 55), (62, 64), (0, 7), (7, 25), (40, 41), (29, 44), (34, 35), (66, 76), (3, 7), (5, 8), (8, 24), (6, 7), (28, 48), (44, 45), (62, 78), (67, 74), (5, 18), (59, 62), (29, 47), (35, 36), (34, 36), (28, 31), (41, 52), (13, 35), (37, 38), (4, 5), (3, 23), (29, 30), (36, 50), (4, 16), (37, 51), (32, 48), (67, 73), (38, 56), (28, 32), (32, 35), (6, 26), (64, 72), (12, 22), (30, 39), (59, 61), (0, 1), (33, 34), (60, 62), (2, 11), (41, 55), (37, 57), (8, 18), (59, 66), (7, 8), (64, 66), (39, 55), (67, 68), (31, 40), (30, 32), (0, 14), (66, 72), (1, 15), (8, 9), (33, 69), (36, 57), (2, 12), (3, 17), (60, 70), (9, 25), (39, 41), (43, 51), (65, 66), (62, 65), (64, 79), (28, 42), (1, 16), (33, 59), (7, 24), (29, 43), (1, 5), (30, 48), (3, 6), (1, 10), (31, 53), (8, 25), (52, 54), (44, 46), (5, 17), (62, 66), (10, 19), (33, 49), (7, 18), (30, 43), (28, 47), (66, 67), (29, 46), (34, 37), (75, 76), (3, 5), (36, 51), (5, 7), (62, 72), (59, 70), (32, 49), (24, 25), (38, 57), (65, 72), (10, 20), (33, 60), (7, 17), (32, 36), (64, 73), (59, 60), (0, 2), (66, 68), (3, 15), (60, 63), (1, 3), (8, 13), (74, 75), (37, 43), (28, 29), (36, 37), (61, 62), (41, 54), (5, 13), (37, 56), (30, 31), (5, 26), (19, 22), (59, 69), (60, 77), (6, 17), (38, 58), (39, 54), (64, 67), (1, 20), (34, 49), (32, 33), (30, 33), (68, 73), (66, 73), (0, 15), (1, 14), (42, 44), (34, 43), (33, 68), (74, 76), (35, 50), (3, 16), (9, 24), (60, 71), (39, 40), (19, 21), (62, 70), (32, 59), (39, 53), (30, 47), (28, 43), (34, 50), (63, 78), (30, 34), (29, 42), (2, 20), (1, 4), (66, 74), (30, 49), (2, 3), (14, 35), (0, 34), (52, 55), (9, 27), (67, 76), (1, 35), (5, 16), (60, 68), (45, 46), (7, 13), (12, 19), (13, 18), (61, 77), (29, 45), (3, 4), (10, 11), (5, 6), (67, 75), (32, 50), (65, 79), (64, 71), (10, 21), (0, 3), (31, 32), (63, 64), (36, 43), (1, 2), (28, 30), (36, 38), (10, 12), (56, 57), (4, 23), (8, 27), (59, 68), (64, 68), (10, 22), (32, 34), (12, 21), (61, 70), (31, 39), (30, 53), (63, 71), (60, 61), (1, 13), (42, 45), (68, 69), (31, 48), (2, 10), (62, 63), (37, 58), (60, 64), (62, 71), (11, 12), (7, 9), (64, 65), (39, 52), (28, 36), (34, 51), (31, 41), (13, 14), (21, 22), (0, 13), (66, 75), (42, 46), (36, 56), (2, 15), (43, 47), (0, 35)}

    exclusions = gc._exclusions
    assert reference == exclusions


def test_names():
    # this test is valid for 2LIQ
    names = gc._names
    reference = ['C1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4', 'C5', 'C6', 'O6', 'C7', 'O7', 'C8', 'OR', 'H1', 'H2', 'H3', 'H4', 'H5', 'H81', 'H2n', 'H82', 'H83', 'H3o', 'H6R', 'H6S', 'H4o', 'H6o', 'C1', 'O1', 'C2', 'N2', 'C3', 'O3', 'C4', 'O4', 'C5', 'C6', 'O6', 'C7', 'O7', 'C8', 'CO1', 'OR', 'HCO1', 'HCO2', 'HCO3', 'H1', 'H2', 'H3', 'H4', 'H5', 'H81', 'H2n', 'H82', 'H83', 'H6R', 'H6S', 'H6o', 'C1', 'C2', 'O2', 'C3', 'O3', 'C4', 'O4', 'C5', 'C6', 'OR', 'H1', 'H2', 'H3', 'H4', 'H5', 'H61', 'H62', 'H63', 'H2o', 'H3o', 'H4o']
    assert reference == names


def test_offsets():
    # this test is valid for 2LIQ
    offsets = gc._offsets
    assert [0, 28, 59, 80, 101] == offsets


def test_set_get_torsionals():
    # check the functions to set and get torsionals one to each other, and also
    # by checking that the energy is the same after changing torsional and
    # then changing them back to original values 
    gc_0 = Glycan('pdbs/2LIQ_min.pdb', linkages=[4, -3])
    a, b, c, d = gc_0.get_phi(0), gc_0.get_psi(0), gc_0.get_phi(1), gc_0.get_psi(1)
    nrg_0 = gc_0.energy()
    for i in range(len(gc) - 1):
        gc_0.set_phi(i, -60.)
        gc_0.set_psi(i, -40.)

    for i in range(len(gc_0) - 1):
        assert_almost_equal(gc_0.get_phi(i), -60.)
        assert_almost_equal(gc_0.get_psi(i), -40.)
        
    gc_0.set_phi(0, a)
    gc_0.set_psi(0, b)
    gc_0.set_phi(1, c)
    gc_0.set_psi(1, d)
    
    nrg_1 = gc_0.energy()
    
    assert_almost_equal(nrg_0, nrg_1)
       
    

        
        

        
          
