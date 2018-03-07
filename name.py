#James Roth
#3/7/18
#name.py - displaying names

from ggame import *
name=input("Enter your name: ")

code=input("Enter an RGB code: ")
color=Color(code, 1)

text=TextAsset(name)
rectangle=RectangleAsset(500,800, color)

Sprite(text, (400,300))
Sprite(rectangle)

App().run()
