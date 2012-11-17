#!/usr/bin/env python
# coding: utf-8
'''
    Simon ANDRÉ ©copyright
    Knack Computer ©copyright
    This file is part of ascii_gimp.

    Foobar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''
from gimpfu import *
import os
from knack.gimp.ascii.utils import KnackError, generate_log_console


class Control(object):
    '''Base class for control gimp'''
    def __init__(self):
        '''Verify if gimp have a loaded img'''
        image_list = gimp.image_list()
        if len(image_list) == 0:
            message = u"Vous devez avoir un image ouverte par gimp pour lancer ce plugins"
            raise KnackError(message)
        self.image = image_list[0]
        self.layer = self.image.layers[0]
    def get_width(self):
        '''return width of current img'''
        return self.image.width
    def get_height(self):
        '''return height of current img'''
        return self.image.height
    def generate_grid(self, columns, row):
        width = self.get_width()
        height = self.get_height()
        if width < columns:
            raise KnackError(u"Votre nom de colones (%i) est superieur au\
 nombre de pixel en largeur (%i) de votre image, opération\
 impossible" % ( int(columns), int(width)))
        if height < row:
            raise KnackError(u"Votre nom de lignes (%i) est superieur au\
 nombre de pixel (%i) en hauteur de votre image, opération\
 impossible" % ( int(row), int(height)))
        self.columns_width = width / columns
        self.row_height = height / row
        return True

class ControlColor(Control):
    def pick_color(self, x, y, width):
        '''return color on current image'''
        return gimp.pdb.gimp_image_pick_color(self.image, self.layer, x, y,
                                                          TRUE , TRUE, widht)
    def check_and_convert(self, grey):
        if grey == 0:
            raise(u"La gestion des images en couleur n'est pas implenté, pardon :-(")
        if self.layer.is_gray:
            return True
        else:
            gimp.pdb.gimp_image_convert_grayscale(self.layer)
            return True
