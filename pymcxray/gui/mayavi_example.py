# Author: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

from mayavi import mlab
from tvtk.tools import visual
from tvtk.api import colors

print("Start")
# Create a figure
f = mlab.figure(size=(500,500))
# Tell visual to use this as the viewer.
visual.set_viewer(f)

print("Before test_plot3D")
# A silly visualization.
mlab.test_plot3d()

print("Before box")
# Even sillier animation.
b1 = visual.box()
b2 = visual.box(x=4., color=colors.red)
b3 = visual.box(x=-4, color=colors.red)
b1.v = 5.0

@mlab.show
@mlab.animate(delay=250)
def anim():
    """Animate the b1 box."""
    print("Start animate")
    while 1:
        b1.x = b1.x + b1.v*0.1
        if b1.x > 2.5 or b1.x < -2.5:
            b1.v = -b1.v
        yield


if __name__ == '__main__':
    # Run the animation.
    print("Run the animation")
    anim()