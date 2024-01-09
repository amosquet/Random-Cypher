# Random-Cypher
A program that encrypts messages so that randos can't just read them, it can also reverse it.

This is the RCCG(Random Caesar Cypher Generator). Meant to simplify the creation of "encrypted" messages allong with decoding them.

RCCG.py contains the encryption scheme and can be called to using RCCG.encode(<message here>) and RCCG.decode(<message here>).
cli.py is a simple script that allows the user to interact with RCCG without a graphical UI, this was how RCCG was initially used.
gui.py is, as the name suggests, a gui for RCCG to make it easier for users to use RCCG through buttons. It will be improved.

Both of these scripts, cli & gui, rely on RCCG.py to run as they call from it to actually encrypt any data.

Check HTI.txt for basic instructions on implementing RCCG

Next course of action is to support capitalization instead of simply converting them to lowercase letters.
I also plan on improving the gui to scale elements with the window size.
Also add comments because I forgot to do that while I was overhauling.

Anybody can suggest or even modify it just let me know if you plan on doing it and share your own version with me, I'd love to see what else other people can think of!

RCCG Created by AlmondMan. Contact: almondman@trollclan.com
Website: https://almondman.trollclan.com/coding-projects/rccg
