#James Roth
#2/8/18
#house.py - using the graphics engine

from ggame import *

blackOutline=LineStyle (0.5, black)
whiteOutline=LineStyle (2, white)

blue=Color(0x8890D5, 1)
blue2=Color(0x2290E8, 1)
red=Color(0xbb0000, 1)

blueSquare=RectangleAsset(300, 125, blackOutline, blue)
blueTriangle=PolygonAsset([(100, 300), (500, 300), (300, 225)], whiteOutline, blue)
blueDoor=RectangleAsset(50, 100, blackOutline, blue2)
redChimney=RectangleAsset(50, 100, blackOutline, red)

Sprite(blueSquare, (200,200))
Sprite(blueTriangle, (150,125))
Sprite(blueDoor, (325, 225))
Sprite(redChimney, (425, 75))

App().run()
