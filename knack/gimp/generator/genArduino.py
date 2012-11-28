#!/usr/bin/env python
# coding: utf-8
'''
    Simon ANDRÉ ©copyright
    Knack Computer ©copyright
    This file is part of knack_gimp_arduino.

    knack_gimp_arduino is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    knack_gimp_arduino is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with knack_gimp_arduino.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
from knack.gimp.utils import KnackError, generate_log_console
from revelation import FileError
from random import uniform

def toDecimal( binaryNumber ):
    multiplier = 0
    number = 0
    for el in binaryNumber[ : : -1 ]:
        number += int( el ) * ( 2**multiplier )
        multiplier += 1
    return number

def toCArray(width, height, pixelList):
    '''generate c array to paste in c/c++ code'''
    code = '#include \"TVOlogo.h\"\n\
PROGMEM const unsigned char TVOlogo[] = {%i,%i,\n%s};' \
    % (width, height, generate_binary_code(pixelList, width, height))
    return code



def generate_binary_code(pixelList, width, height):
    '''convert pixel list to hexadecimal'''
    hexacode = str()
    binary = ''
    index_row = 0
    index_break_line = 0
    for pixel in pixelList:
        index_row += 1
        index_break_line += 1  
        if pixel == 0:
            binary += '0'
        else:
            '''pixel==255'''
            binary += '1'
        if index_row >= width:
            binary = binary.ljust(8, '0')
            index_row = 0
        if len(binary) == 8:
            hexacode += hex(toDecimal(binary))
            hexacode += ','
            if index_break_line >= width:
                hexacode += '\n'
                index_break_line = 0
            binary = ''
    if len(binary) != 0:
        hexacode += hex(toDecimal(binary))
        hexacode += ','
    return hexacode[:-1]
    
class genArduino(object):
    def __init__(self):
        None
    def generate(self, width, height, pixelList, output_file):
        '''generate cpp file with binary'''
        generate_log_console(file)
        try:
            node = open(output_file, 'w')
        except IOError as e:
            raise KnackError("I/O error({0}): {1}".format(e.errno, e.strerror))
        else:
            node.write(toCArray(width, height, pixelList))
        finally:
            node.close()
        return True
