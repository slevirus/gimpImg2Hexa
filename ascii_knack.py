#!/usr/bin/env python
# coding: utf-8
''''''

from gimpfu import *
import os

def run(*args):
    """main plugin"""
    input_dir, output_dir = args
    image = gimp.image_list()[0]
    layer = image.layers[0]


register(
    "ascii_knack", "", "", "", "", "",
    "<Toolbox>/Xtns/Languages/Python-Fu/knack/ascii knack", "",
    [
    (PF_DIRNAME, "arg0", "Repertoire avec les images sources", ""),
    (PF_STRING, "arg1", "Nom du fichier", ""),
    ],
    [],
    run,
    )

main()
