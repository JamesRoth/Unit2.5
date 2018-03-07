#James Roth
#3/7/18
#name.py - displaying names

from ggame import *
name=input("Enter your name: ")

code=input("Enter an RGB code: ")
color=Color(code, 1)
outline=LineStyle(1, color)

text=TextAsset(name)
rectangle=RectangleAsset(500, 1600, outline, color)

Sprite(rectangle)
Sprite(text, (400,300))

App().run()
