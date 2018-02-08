#James Roth
#2/8/18
#house.py - using the graphics engine

from ggame import *

blackOutline=LineStyle (0.5, black)

blue=Color(0x0000ff, 1)

blueSquare=RectangleAsset(300, 125, blackOutline, blue)

Sprite(blueSquare, (200,200))

App().run()
