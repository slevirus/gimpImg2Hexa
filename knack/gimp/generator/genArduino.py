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

def toCArray(width, height, pixelList):
    '''generate c array to paste in c/c++ code'''
    generate_log_console(pixelList.__repr__())
    code = '{%i,%i,%s}' % (width, height, generate_hexacode(pixelList))
    return code

def generate_hexacode(pixelList):
    hexacode = str()
    for pixel in pixelList:
        hexacode += pixel
        hexacode += ','
    return hexacode[:-1]

class genArduino(object):
    def __init__(self):
        None
    def generate(self, width, height, pixelList):
        code = toCArray(width, height, pixelList)
        generate_log_console(code)

