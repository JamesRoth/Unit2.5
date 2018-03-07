#James Roth
#3/7/18
#yield.py - yield sign

from ggame import *

red=Color(0xff0000, 1)
white=Color(0xffffff, 1)
whiteOutline=LineStyle(1, white)
redOutline=LineStyle(1, red)

whiteTriangle=PolygonAsset([(10,10), (490,10), (250,490)], whiteOutline, white)
redTriangle=PolygonAsset([(0,0), (500,0), (250,500)], redOutline, red)

Sprite(redTriangle)
Spite(whiteTriangle)

App().run()
