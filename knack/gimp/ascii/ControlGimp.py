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
from knack.gimp.ascii.Gen import GenAscii

class ControlGimp(object):
    '''Base class for control gimp'''
    def __init__(self):
        '''Verify if gimp have a loaded img'''
        image_list = gimp.image_list()
        if len(image_list) == 0:
            message = u"Vous devez avoir un image ouverte par gimp pour lancer ce plugins"
            raise KnackError(message)
        self.image = image_list[0]
        self.layer = self.image.layers[0]

class ControlCoord(ControlGimp):
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
            raise KnackError(u"Votre nom de colonnes (%i) est superieur au\
 nombre de pixel en largeur (%i) de votre image, opération\
 impossible" % ( int(columns), int(width)))
        if height < row:
            raise KnackError(u"Votre nom de lignes (%i) est superieur au\
 nombre de pixel (%i) en hauteur de votre image, opération\
 impossible" % ( int(row), int(height)))
        self.columns_width = width / columns
        self.row_height = height / row
        self.row = row
        self.columns = columns
        if self.columns_width < self.row_height:
            self.radius = self.columns_width
        else:
            self.radius = self.row_height
        return True
    def make_rectangle_selection(self):
        '''create new rectangle selection'''
        gimp.pdb.gimp_image_set_active_layer(self.image, self.layer)
        gimp.pdb.gimp_selection_none(self.image)
        gimp.pdb.gimp_image_select_rectangle(self.image, CHANNEL_OP_REPLACE, \
                                             x, y, AVERAGE_WIDTH_PIX, AVERAGE_WIDTH_PIX)
        return True
    def make_total_selection(self):
        '''create selection scale to all image aera'''
        gimp.pdb.gimp_image_set_active_layer(self.image, self.layer)
        gimp.pdb.gimp_selection_none(self.image)
        gimp.pdb.gimp_selection_all(self.image)
        return True
    
class ControlLayer(ControlCoord):
    def create_working_layer(self):
        self.make_total_selection()
        self.copy_paste()
        return
    def copy_paste(self):
        '''make copy of the selection and paste it in a new layer'''
        gimp.pdb.gimp_edit_copy(self.layer)
        floating_sel = gimp.pdb.gimp_edit_paste(self.layer, TRUE)
        gimp.pdb.gimp_floating_sel_to_layer(floating_sel)
        self.layer = self.image.layers[0]
        pdb.gimp_image_set_active_layer(self.image, self.layer)
        return True
    def delete_layer(self):
        pdb.gimp_image_remove_layer(self.image, self.layer)
        self.layer = self.image.layers[0]
        return True

class ControlColor(ControlLayer):
    def pick_color(self, x, y, width):
        '''return color picked on current image'''
        self.color_picked = gimp.pdb.gimp_image_pick_color(self.image, self.layer, x, y,
                                                          TRUE , TRUE, width)
    def pick_gray(self, x, y, width):
        '''return color picked on current image'''
        self.pick_color(x, y, width)
        if self.color_picked[0] == self.color_picked[1] \
                    and self.color_picked[0] == self.color_picked[2]:
            self.gray = self.color_picked[0]
        else:
            raise KnackError(u"L'image n'est pas conveti en niveau de gris ?")
        return True
    def check_and_convert(self, grey):
        '''Convert layer color if needed'''
        if grey == 0:
            raise(u"La gestion des images en couleur n'est pas implenté, pardon :-(")
        if self.layer.is_gray:
            return True
        else:
            gimp.pdb.gimp_image_convert_grayscale(self.image)
            return True
    def make_list_color(self):
        '''make list with color'''
        self.list_color = []
        for y in range(0, self.get_height(), self.row_height):
            for x in range(0, self.get_width(), self.columns_width):
                self.pick_gray(x, y, self.radius)
                self.list_color.append(self.gray)
            #add '\n' for line break
            self.list_color.append(13)

class Control(ControlColor):
    def __init__(self):
        '''instanciate ascii generator'''
        self.generator_ascii = GenAscii()
        return super(Control, self).__init__()
    def generate_ascii(self, filename):
        '''lauch file generator process with ascii generator'''
        self.make_list_color()
        self.generator_ascii.generate_ascii(self.list_color, filename)