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


class KnackError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        '''return str representation of message error'''
        return repr(self.value)
    def generate_log_console(self):
        '''log on console windows in gimp'''
        handler = gimp.pdb.gimp_message_get_handler()
        gimp.pdb.gimp_message_set_handler(2)
        gimp.pdb.gimp_message(self.value)
        gimp.pdb.gimp_message_set_handler(handler)
        return True
    def generate_log_popup(self):
        '''log on popup windows in gimp'''
        handler = gimp.pdb.gimp_message_get_handler()
        gimp.pdb.gimp_message_set_handler(0)
        gimp.pdb.gimp_message(self.value)
        gimp.pdb.gimp_message_set_handler(handler)
        return True

def generate_log_console(error_str):
    '''log on console windows in gimp'''
    handler = gimp.pdb.gimp_message_get_handler()
    gimp.pdb.gimp_message_set_handler(2)
    gimp.pdb.gimp_message(error_str)
    gimp.pdb.gimp_message_set_handler(handler)
    return True