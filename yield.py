#James Roth
#3/7/18
#yield.py - yield sign

from ggame import *

red=Color(0xff0000, 1)
white=Color(0xffffff, 1)
whiteOutline=LineStyle(1, white)
redOutline=LineStyle(1, red)

whiteTriangle=PolygonAsset([(30,20), (460,20), (250,470)], whiteOutline, white)
redTriangle=PolygonAsset([(0,0), (500,0), (250,500)], redOutline, red)

Sprite(redTriangle)
Sprite(whiteTriangle, (30, 20))

App().run()
