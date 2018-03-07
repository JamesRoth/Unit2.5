#James Roth
#3/7/18
#yield.py - yield sign

red=Color(0xff0000, 1)
redOutline=LineStyle(red, 1)

redTriangle=PolygonAsset([(0,0), (300, 0), (150, 100)], redOutline, red)

Sprite(redTriangle)

App().run()
