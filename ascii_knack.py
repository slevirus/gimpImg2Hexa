#!/usr/bin/env python
# coding: utf-8
''''''

from gimpfu import *
import os

def run(*args):
    """main plugin"""
    input_dir, filename, use_char, width, height = args
    generate_log(input_dir)
    generate_log(filename)
    generate_log(use_char)
    generate_log(width)
    generate_log(height)
    image = gimp.image_list()[0]
    layer = image.layers[0]
    list_char = split_use_char(use_char)


def split_use_char(use_char):
    #use_char = str()
    use_char = use_char.strip()
    generate_log(use_char)
    use_char = use_char.split(';')
    generate_log(use_char)
    
    

def generate_log(error_str):
    '''log on console windows in gimp'''
    handler = gimp.pdb.gimp_message_get_handler()
    gimp.pdb.gimp_message_set_handler(2)
    gimp.pdb.gimp_message(error_str)
    gimp.pdb.gimp_message_set_handler(handler)
    return True

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
