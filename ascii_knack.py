#!/usr/bin/env python
# coding: utf-8
''''''

from gimpfu import *
import os
from knack.gimp.ascii import ControlGimp
from knack.gimp.ascii import utils

def run(*args):
    """main plugin"""
    input_dir, filename, use_char, width, height = args
    utils.generate_log(input_dir)
    utils.generate_log(filename)
    utils.generate_log(use_char)
    utils.generate_log(width)
    utils.generate_log(height)
    image = gimp.image_list()[0]
    layer = image.layers[0]
    list_char = split_use_char(use_char)


def split_use_char(use_char):
    #use_char = str()
    use_char = use_char.strip()
    utils.generate_log(use_char)
    use_char = use_char.split(';')
    utils.generate_log(use_char)
    
    



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
