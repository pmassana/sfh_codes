import numpy as np
from astropy.io import fits, ascii
import sys

input_file = str(sys.argv[1])
mother_name = np.loadtxt(input_file, dtype = 'str')

mother_original = np.loadtxt(str(mother_name), usecols=(1, 3, 11, 13))

ageb = [0., 0.5, 1., 1.5, 2., 2.5, 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14.]
metb = [0.0004, 0.0007, 0.0011, 0.0016, 0.0022, 0.0029, 0.0037, 0.0046, 0.0056, 0.0067, 0.0079, 0.0092, 0.0106, 0.0122, 0.0140, 0.0160, 0.0182, 0.0206, 0.0232, 0.0260, 0.0290]

age = np.power(10.0, mother_original.T[0] - 9.0)
met = mother_original.T[1]

burst_1 = np.where((age > 0.0) & (age < 0.5) & (met > 0.0160) & (met < 0.0182))
burst_2 = np.where((age > 0.0) & (age < 0.5) & (met > 0.0160) & (met < 0.0182))
burst_3 = np.where((age > 0.0) & (age < 0.5) & (met > 0.0160) & (met < 0.0182))
burst_4 = np.where((age > 0.0) & (age < 0.5) & (met > 0.0160) & (met < 0.0182))

n1 = len(burst_1)
n2 = len(burst_2)
n3 = len(burst_3)
n4 = len(burst_4)
