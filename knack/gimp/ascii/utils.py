










from gimpfu import *

def generate_log_console(error_str):
    '''log on console windows in gimp'''
    handler = gimp.pdb.gimp_message_get_handler()
    gimp.pdb.gimp_message_set_handler(2)
    gimp.pdb.gimp_message(error_str)
    gimp.pdb.gimp_message_set_handler(handler)
    return True

def generate_log_popup(error_str):
    '''log on console windows in gimp'''
    handler = gimp.pdb.gimp_message_get_handler()
    gimp.pdb.gimp_message_set_handler(0)
    gimp.pdb.gimp_message(error_str)
    gimp.pdb.gimp_message_set_handler(handler)
    return True