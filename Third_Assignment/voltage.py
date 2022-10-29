import numpy 
from scipy import interpolate
from matplotlib import pyplot as plt

class VoltageData:
    """Class for handling a sequence of voltage measurements taken at 
    different times.
    """

    def __init__(self, times, voltages):
        """Class constructor. Times and voltages are iterables of the same
        length.
        """
        times = numpy.array(times, dtype=numpy.float64)
        voltages = numpy.array(voltages, dtype=numpy.float64)
        self.data = numpy.column_stack([times, voltages])
        #if len(self.times != self.voltages):
            #raise ValueError('Times and voltages must be of the same lenght!')
        self._spline = interpolate.InterpolatedUnivariateSpline(times, voltages, k=3)
    
    @classmethod
    def from_file(cls, data_path):
        """Constructor from a file
        """
        times, voltages = numpy.loadtxt(data_path, unpack=True)
        return cls(times, voltages)

    @property
    def times(self):
        return self.data[:, 0]

    @property
    def voltages(self):
        return self.data[:, 1]
    
    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        #for row in enumerate(self):
        #    line = f'[i] -> {row[0]} {row[1]} \n'
        #    output_str += line
        #return output_str

        header = 'Row -> Time [s] Voltage [mV] \n'

        return  header + '\n'.join([f'[{i}] -> {row[0]} {row[1]}' for i, row in enumerate(self)])

    def __repr__(self):
        return '\n'.join([f'{row[0]} {row[1]}' for row in self])

    def __call__(self, t):
        return self._spline(t)

    def plot(self, ax=None, draw_spline=False, **plot_opts):
        if ax is None:
            plt.figure('voltage_vs_time')
        else:
            plt.sca(ax)
        plt.plot(self.times, self.voltages, **plot_opts)
        plt.xlabel('Times [s]')
        plt.ylabel('Voltages [mV]')
        if draw_spline:
            x = numpy.linspace(min(self.times), max(self.times), 100)
            plt.plot(x, self(x), '-')



if __name__ == '__main__':
    """
    """

    vdata = VoltageData.from_file('data.txt')

    #print(vdata.times, vdata.voltages)

    for element in vdata:
        print(element)

    print(vdata)   
    
    vdata.plot()
    plt.show()