#!/usr/bin/env python
# coding: utf-8
'''
    Simon ANDRÉ ©copyright
    Knack Computer ©copyright
    This file is part of knack_ascii_gimp.

    knack_ascii_gimp is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    knack_ascii_gimp is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with knack_ascii_gimp.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
from knack.gimp.ascii.utils import KnackError, generate_log_console
from revelation import FileError


class GenAscii(object):
    def __init__(self, mode='file'):
        if mode == 'file' or mode == 'term':
            self.mode = mode
        else:
            raise KnackError(u"Le mode de rendu doit être file ou term !!!")
    def load_char(self, list_char=None, list_color=None):
        if list_char == None:
            return True
        else:
            raise KnackError(u"La génération d'une séléction de charactère n'est pas implémenté")
        
    def generate_ascii(self, list_color, filename):
        if self.mode=='file':
            try:
                node = open(filename, 'w')
            except IOError as e:
                raise KnackError("I/O error({0}): {1}".format(e.errno, e.strerror))
            else:
                for color in list_color:
                    node.write(chr(color))
            finally:
                node.close()
            
            return True
        else:
            raise KnackError(u"la génération d'ascii ne peut actuellement se faire que dans un fichier")
        

