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
    def generate(self, width, height, pixelList, directory, projectname):
        try:
            path_src = self.generateInoProject(directory, projectname)
        except KnackError as e:
            e.generate_log_popup()
        try:
            node = open(os.path.join(path_src, 'bitmaps.cpp'), 'w')
        except IOError as e:
            raise KnackError("I/O error({0}): {1}".format(e.errno, e.strerror))
        else:
            node.write(toCArray(width, height, pixelList))
        finally:
            node.close()
        return True
    def generateInoProject(self, directory, projectname):
        os.chdir(directory)
        os.mkdir(projectname, 0770)
        os.chdir(os.path.join(directory, projectname))
        os.mkdir('src', 0770)
        os.chdir(os.path.join(directory, projectname, 'src'))
        return os.path.join(directory, projectname, 'src')
        
