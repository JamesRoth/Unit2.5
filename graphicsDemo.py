#James Roth
#2/7/18
#graphicsDemo.py - intro to ggame

from ggame import *

red=Color(0xff0000, 1) #this is the color red
black=Color(0x000000, 1) #this is the color black
green=Color(0x00ff00, 1) 
blue=Color(0x0000ff, 1)

blackOutline=LineStyle(1,black)

redRectangle=RectangleAsset(200,100,blackOutline,red) #(width, height, outline, fill color)
blueCircle=CircleAsset(75, blackOutline, blue) #(radius, outline, fill color)
greenEllipse=EllipseAsset(100, 50, blackOutline, green) #(width, height, outline, fill color)

Sprite(redRectangle)
Sprite(blueCircle,(100, 100)) #Sprite(spriteName, (x, y))
Sprite(greenEllipse, (200, 400))

App().run()
