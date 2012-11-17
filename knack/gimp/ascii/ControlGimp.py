



from gimpfu import *
import os
from knack.gimp.ascii.utils import KnackError



class Control(object):
    def __init__(self):
        image_list = gimp.image_list()
        if len(image_list) == 0:
            message = u"Vous devez avoir un image ouverte par gimp pour lancer ce plugins"
            raise KnackError(message)
        self.image = image_list[0]
        self.layer = image.layers[0]
        
    def get_width(self):
        return self.image.width
    def get_height(self):
        return self.image.height


class ControlColor(Control):
    def pick_color(self, x, y, width):
        #self.generate_log('center_x: %s , center_y : %s' % (self.coord.center_x, self.coord.center_y))
        return gimp.pdb.gimp_image_pick_color(self.image, self.layer, x, y,
                                                          TRUE , TRUE, widht)
