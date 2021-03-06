#!/usr/bin/env python
# coding: utf-8
'''
    Simon ANDRÉ ©copyright
    Knack Computer ©copyright
    This file is part of knack_gimp_ascii.

    knack_gimp_ascii is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    knack_gimp_ascii is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with knack_gimp_ascii.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
from knack.gimp.utils import KnackError, generate_log_console
from revelation import FileError
from random import uniform


class genAscii(object):
    def __init__(self, mode='file'):
        if mode == 'file' or mode == 'term':
            self.mode = mode
        else:
            raise KnackError(u"Le mode de rendu doit être file ou term !!!")
        
    def mapp_char(self, select_color=[]):
        mapp_dict = {}
        for color in select_color:
            if color == 10 or color > 32 and color < 126:
                mapp_dict[color] = chr(color)
            else:
                mapp_dict[color] = chr(int(round(uniform(32,126), 0)))
        return mapp_dict
        
    def generate(self, list_color, select_color, filename):
        if self.mode=='file':
            try:
                node = open(filename, 'w')
            except IOError as e:
                raise KnackError("I/O error({0}): {1}".format(e.errno, e.strerror))
            else:
                mapp_dict = self.mapp_char(select_color)
                for color in list_color:
                    node.write(mapp_dict[color])
            finally:
                node.close()
            return True
        else:
            raise KnackError(u"la génération d'ascii ne peut actuellement se faire que dans un fichier")
        

