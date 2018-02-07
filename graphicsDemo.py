#James Roth
#2/7/18
#graphicsDemo.py - intro to ggame

from ggame import *

red=Color(0xff0000, 1) #this is the color red
black=Color(0x000000, 1) #this is the color black

blackOutline=Linesytle(1,black)

redRectangle=RectangleAsset(200,100,blackOutline,red) #(width, height, outline, fill color)

Sprite(redRectangle)

App().run()
