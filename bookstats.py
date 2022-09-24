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

"""First assignment for the CMEPDA course, 2022/23.
"""

import argparse
import time
import numpy as np
from matplotlib import pyplot as plt

def process(file_path):
    """Gives back the relative frequency of letters in a book"""
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    letters = []
    total = 0.
    for i in range(97, 123):
        lower_letter = text.count(chr(i))
        upper_letter = text.count(chr(i-32))
        increase = lower_letter+upper_letter
        letters.append(increase)
        total += increase
        #print(f'Number of {chr(i-32)}\'s counted = ', n+m)
    for i in range(97, 123):
        letters[i-97] /= total
        print(f'Relative frequency of {chr(i-32)}\'s = ', letters[i-97])
    alphabet = list(map(chr, range(97, 123)))
    arr = np.array(letters)
    plt.bar(alphabet, arr)
    plt.title('Letters relative frequencies of occurrance')
    plt.show()

START = time.time()

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Print some book statistics')
    PARSER.add_argument('infile', type=str, help='path to the input file')
    ARGS = PARSER.parse_args()
    process(ARGS.infile)

END = time.time() - START
print(f'Time elapsed from start = {END} seconds')
