#!/usr/bin/env python
# coding: utf-8
''''''

from gimpfu import *
import os
from knack.gimp.ascii.utils import generate_log_console, generate_log_popup
from knack.gimp.ascii.ControlGimp import ControlColor


def run(*args):
    """main plugin"""
    input_dir, filename, use_char, width, height = args
    generate_log_console(input_dir)
    generate_log_console(filename)
    generate_log_console(use_char)
    generate_log_console(width)
    generate_log_console(height)
    image_list = gimp.image_list()
    if len(image_list) == 0:
        message = u"Vous devez avoir un image ouverte par gimp pour lancer ce plugins"
        generate_log_popup(message)
        return False
    image = image_list[0]
    layer = image.layers[0]
    list_char = split_use_char(use_char)
    control_object = ControlColor()


def split_use_char(use_char):
    #use_char = str()
    use_char = use_char.strip()
    generate_log_console(use_char)
    use_char = use_char.split(';')
    generate_log_console(use_char)
    return use_char
    
    



register(
    "ascii_knack", "", "", "", "", "",
    "<Toolbox>/Xtns/Languages/Python-Fu/knack/ascii knack", "",
    [
    (PF_DIRNAME, "arg0", "Repertoire avec les images sources", ""),
    (PF_STRING, "arg1", "Nom du fichier", ""),
    (PF_STRING, "arg2", "caractere utilise", ""),
    (PF_INT, "arg3", "largeur en pixel", ""),
    (PF_INT, "arg4", "hauteur en pixel", ""),
    ],
    [],
    run,
    )

main()
