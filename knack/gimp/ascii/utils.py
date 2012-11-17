from gimpfu import *


class KnackError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    def generate_log_console(self):
        '''log on console windows in gimp'''
        handler = gimp.pdb.gimp_message_get_handler()
        gimp.pdb.gimp_message_set_handler(2)
        gimp.pdb.gimp_message(self.value)
        gimp.pdb.gimp_message_set_handler(handler)
        return True
    def generate_log_popup(self):
        '''log on console windows in gimp'''
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