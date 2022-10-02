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
from matplotlib import pyplot as plt

def process(file_path, hist='hist'):
    """Gives back the relative frequency of letters in a book"""
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read().lower()
    total = 0.
    alpha = {}
    for i in range(97, 123):
        alpha[chr(i)] = text.count(chr(i))
        total += alpha[chr(i)]
    for i in range(97, 123):
        alpha[chr(i)] /= total
        print(f'Relative frequency of {chr(i-32)}\'s = ', alpha[chr(i)])
    if hist:
        plt.bar(alpha.keys(), alpha.values())
        plt.title('Letters relative frequencies of occurrance')
        plt.show()

START = time.time()

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Show the relative\
         frequency of every english letter in a book')
    PARSER.add_argument('infile', type=str, help='path to the input file')
    PARSER.add_argument('-hist', type=str, help='show a histogram of every\
         letter relative frequency')
    ARGS = PARSER.parse_args()
    process(ARGS.infile, ARGS.hist)

END = time.time() - START
print(f'Time elapsed from start = {END} seconds')
