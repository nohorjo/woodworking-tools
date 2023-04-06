from solid import *
from solid.utils import *

from constants import *
from super_hole import *

if __name__ == '__main__':
    size: float = 100.0
    thickness: float = 20.0
    height: float = 35.0

    model = square(size)
    model -= translate([thickness, thickness])(square(size))
    model = linear_extrude(height)(model)

    scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])

