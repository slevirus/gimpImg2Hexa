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

from gimpfu import *
import os
from knack.gimp.utils import KnackError, generate_log_console
from knack.gimp.control.controlGimp import control
from knack.gimp.generator.genArduino import genArduino




def run(*args):
    """main plugin"""
    input_dir, filename = args
    filePath = os.path.join(input_dir, filename)
    try:
        control_object = control(genArduino())
        control_object.make_total_selection()
        control_object.check_and_convert_1bit()
        control_object.generate_bitmap(filePath)
    except KnackError as e:
        e.generate_log_popup()
        return False


register(
    "knack_gimp_arduino", "", "", "", "", "",
    "<Toolbox>/Xtns/Languages/Python-Fu/knack/arduino", "",
    [
    (PF_DIRNAME, "arg0", u"Repertoire du projet (sketchbook)", ""),
    (PF_STRING, "arg1", "Nom du projet", u"myproject"),
    ],
    [],
    run,
    )

main()
