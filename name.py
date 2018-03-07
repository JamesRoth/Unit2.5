#James Roth
#3/7/18
#name.py - displaying names

from ggame import *
name=input("Enter your name: ")
color=Color("0x" + input("Enter an RGB code: "), 1)

text=TextAsset(name, fill=color)

Sprite(text, (300,300))

App().run()
