



from gimpfu import *
import os




class Control(object):
    def __init__(self):
        self.image = gimp.image_list()[0]
        self.layer = self.image.layers[0]
        return
    def generate_log(self, message):
        return
    def get_width(self):
        return self.image.width
    def get_height(self):
        return self.image.height


class ControlColor(Control):
    def pick_color(self, x, y, width):
        self.generate_log('center_x: %s , center_y : %s' % (self.coord.center_x, self.coord.center_y))
        return gimp.pdb.gimp_image_pick_color(self.image, self.layer, x, y,
                                                          TRUE , TRUE, widht)
