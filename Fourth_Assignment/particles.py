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
# along with this program.  If not, see <https://www.gnu.org/licenses/>

import math

class Particle():

    def __init__(self, mass, charge, name, momentum=0.):
        if(mass > 0.):
            self._mass = float(mass) #massa in MeV
        else:
            raise ValueError('Particle mass is not positive!') 
        if(type(charge) == int):
            self._charge = int(charge) #carica in unità di carica elettronica
        else:
            raise ValueError('Particle charge is not an integer!')
        self._name = str(name)
        if(momentum >= 0.):
            self._momentum = momentum
        else:
            raise ValueError('Particle momentum is negative!')
    

    @property
    def mass(self):
        return self._mass
    
    @property
    def name(self):
        return self._name
    
    @property
    def charge(self):
        return self._charge

    @property
    def energy(self):
        return math.sqrt(self.momentum**2 + self.mass**2)

    @energy.setter
    def energy(self, value):
        if(value < self.mass):
            print(f'Particle energy is less than its mass {self.mass} MeV!')
            return
        self.momentum = math.sqrt(value**2 - self.mass**2)

    @property
    def momentum(self):
        return self._momentum
        

    @momentum.setter
    def momentum(self, value):
        if(value < 0.):
            print('Momentum is negative! Use a non-negative value')
            return
        else:
            self._momentum = value

    @property
    def beta(self):
        return self.momentum / math.sqrt(self.momentum**2 + self.mass**2)
        
    @beta.setter
    def beta(self, value):
        if(value < 0.) or (value >= 1.):
            print('Beta of particle is not between 0 and 1!')
            return
        else:
            self.momentum = value * self.mass / math.sqrt(1. - value**2)

    @property
    def gamma(self):
        return math.sqrt(self.momentum**2 + self.mass**2) / self.mass

    @gamma.setter
    def gamma(self, value):
        if(value < 0.):
            print('Gamma of particle is less than zero!')
            return
        else:
            self.momentum = self.mass * math.sqrt(value**2 - 1.)


    def __repr__(self):
        return f'Particle: {self.name}, mass= {self.mass} MeV, charge= {self.charge:+}e, \n \
        energy= {self.energy:.2f} MeV, momentum= {self.momentum:.2f} MeV, \n beta= {self.beta:.2f}, gamma= {self.gamma:.2f}'

    


    
class Proton(Particle):

    NAME = 'Proton'
    MASS = 938.27 #MeV
    CHARGE = +1 #e

    def __init__(self, momentum=0.):
        super().__init__(self.MASS, self.CHARGE, self.NAME, momentum)


class Alfa(Particle):

    NAME = 'Alfa'
    MASS = 3727.3 #MeV
    CHARGE = +4 #e

    def __init__(self, momentum=0.):
        super().__init__(self.MASS, self.CHARGE, self.NAME, momentum)
    