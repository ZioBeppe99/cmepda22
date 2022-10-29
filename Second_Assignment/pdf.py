#!/usr/bin/env python
# Copyright (C) 2022 g.fanciulli2@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunciton(InterpolatedUnivariateSpline):

    def __init__(self, x, y):
        """Constructor
        """
        norm = InterpolatedUnivariateSpline(x, y).integral(x[0], x[-1])
        y /= norm
        super().__init__(x, y)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)

        xppf, ippf = np.unique(ycdf, return_index=True) #restituisce un array xppf con il valori di ycdf \che non si ripetono e ad ognuno di essi associa un indice ippf
        yppf = x[ippf] #crea un array dove le yppf sono le x non ripetute due volte
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf)

    def prob(self, a, b):
        """Return the probability for the random variable to be between a and b.
        """
        return self.cdf(b) - self.cdf(a) 
 
    def distribution(self, size):
        return self.ppf(np.random.uniform(size=size))



if __name__ == '__main__':
        x = np.linspace(0., 1., 50)
        y = x
        pdf = ProbabilityDensityFunciton(x, y)

        
        plt.plot(x, y, 'o')
        plt.plot(x, pdf.cdf(x), label='spline')
        plt.plot(x, pdf.ppf(x), label='spline')
        #plt.hist(pdf.distribution(1000000), bins=200)
        plt.plot(x, pdf(x), label='spline')
        plt.legend()
        plt.show()