#James Roth
#2/9/18
#Germany.py - making a german flag

from ggame import *

red=Color(0xff0000,1)
yellow=Color(0xffff00,1)
black=Color(0x000000,1)

noOutline=LineStyle(0, black)

bar1=RectangleAsset(500, 90, noOutline, black)
bar2=RectangleAsset(500, 90, noOutline, red)
bar3=RectangleAsset(500, 90, noOutline, yellow)

Sprite(bar1, (0,0))
Sprite(bar2, (0,90))
Sprite(bar3, (0,180))

App().run()