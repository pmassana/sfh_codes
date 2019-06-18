import numpy as np
from astropy.io import fits, ascii
import sys

input_file = str(sys.argv[1])
input_data = ascii.read(input_file)

mother_name = input_data['mother_file']

mother_original = ascii.read(mother_name)

ageb = [0., 0.5, 1., 1.5, 2., 2.5, 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14.]
metb = [0.0004, 0.0007, 0.0011, 0.0016, 0.0022, 0.0029, 0.0037, 0.0046, 0.0056, 0.0067, 0.0079, 0.0092, 0.0106, 0.0122, 0.0140, 0.0160, 0.0182, 0.0206, 0.0232, 0.0260, 0.0290]


