import unittest
import sys

from matplotlib import pyplot as plt

if sys.flags.interactive:
    plt.ion()

from particles import Particle
from particles import Proton
from particles import Alfa

class TestParticle(unittest.TestCase):

    def test_particle(self):
        mass = 3727
        charge = -2
        name = 'alfa'
        momentum = 200

        particle = Particle(mass, charge, name, momentum=momentum)
        self.assertTrue(particle.mass==mass)
        self.assertTrue(particle.charge==charge)
        self.assertTrue(particle.name==name)
        self.assertTrue(particle.momentum==momentum)
        
        particle.mass = 345
        
        



        
if __name__ == '__main__':
    unittest.main(exit=not sys.flags.interactive)        

    
        



