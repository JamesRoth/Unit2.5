#James Roth
#3/7/18
#yield.py - yield sign

from ggame import *

red=Color(0xff0000, 1)
redOutline=LineStyle(1, red)

redTriangle=PolygonAsset([(0,0), (300,0), (150,100)], redOutline, red)

Sprite(redTriangle)

App().run()
