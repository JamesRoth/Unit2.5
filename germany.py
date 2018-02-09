#James Roth
#2/9/18
#Germany.py - making a german flag

from ggame import *

red=Color(0xff0000)
yellow=Color(0xffff00)
black=Color(0x000000)

noOutline=LineStyle(black, 0)

bar1=RectangeAsset(500, 100, noOutline, black)
bar2=RectangeAsset(500, 100, noOutline, red)
bar3=RectangeAsset(500, 100, noOutline, yellow)

Sprite(bar1, (0,0))
Sprite(bar2, (0,100))
Sprite(bar3, (0,200))

App().run()