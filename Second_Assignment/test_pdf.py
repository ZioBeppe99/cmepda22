import unittest
import sys

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
if sys.flags.interactive: #run normale o in modalità interattiva, ovvero con plot
    plt.ion()

from pdf import ProbabilityDensityFunciton

class TestPdf(unittest.TestCase):
    """
    """

    def test_uniform(self): #test con  distribuzione uniforme
        """
        """
        x = np.linspace(0., 1., 100)
        y = np.full(x.shape, 1.)
        pdf = ProbabilityDensityFunciton(x, y)
        self.assertAlmostEqual(pdf(0.5), 1.)  #test che la pdf faccia 1. in ogni punto
        self.assertAlmostEqual(pdf.integral(0., 1.), 1.)
        self.assertAlmostEqual(pdf.prob(0.25, 0.75), 0.5)
        print(pdf)
        


if __name__ == '__main__':
    unittest.main(exit=not sys.flags.interactive)        
