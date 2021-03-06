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

from gimpfu import *
import os
from knack.gimp.utils import KnackError, generate_log_console
from knack.gimp.control.controlGimp import control
from knack.gimp.generator.genAscii import genAscii
from knack.gimp.generator.genArduino import genArduino


def run(*args):
    """main plugin"""
    input_dir, filename, width, height, grey = args
    try:
        control_object = control(genAscii())
        control_object.generate_grid(width, height)
        control_object.check_and_convert(grey)
        control_object.create_working_layer()
        control_object.generate_ascii(os.path.join(input_dir, filename))
    except KnackError as e:
        e.generate_log_popup()
        return False



register(
    "knack_gimp_ascii", "", "", "", "", "",
    "<Toolbox>/Xtns/Languages/Python-Fu/knack/ascii knack", "",
    [
    (PF_DIRNAME, "arg0", u"Repertoire de sortie", ""),
    (PF_STRING, "arg1", "Nom du fichier", u"filename.txt"),
    (PF_INT, "arg3", "nombre de colonne", u"30"),
    (PF_INT, "arg4", "nombre de ligne", u"10"),
    (PF_TOGGLE, "arg5", "niveau de gris", 1),
    ],
    [],
    run,
    )

main()
