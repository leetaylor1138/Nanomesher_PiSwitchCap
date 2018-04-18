#!/usr/bin/env python

# This is a demo to show ip address of eth0 and wlan0 network interace on the ProdBoard OLED Display

'''
Copyright [2017] [Nanomesher Limited - www.nanomesher.com]

Licensed under the Apache License, Version 2.0 (the "License"); you may not use$

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed$
'''


from __future__ import unicode_literals

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from PIL import ImageFont
from subprocess import *
import os
import time

serial = i2c(port=1, address=0x3C)


def GetLANIP():
   try:
     cmd = "ip addr show eth0 | grep inet  | grep -v inet6 | awk '{print $2}' | cut -d '/' -f 1"
     p = Popen(cmd, shell=True, stdout=PIPE)
     output = p.communicate()[0]
     ip = output[:-1]
     if(ip ==""):
        return "-"
     else:
        return ip
   except:
     return "-"
	 
def GetWLANIP():
   try:
     cmd = "ip addr show wlan0 | grep inet  | grep -v inet6 | awk '{print $2}' | cut -d '/' -f 1"
     p = Popen(cmd, shell=True, stdout=PIPE)
     output = p.communicate()[0]
     ip = output[:-1]
     if(ip ==""):
        return "-"
     else:
        return ip
   except:
     return "-"

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

try:
        #device = sh1106(serial, rotate=0)
        device = ssd1306(serial, rotate=0)

        hasOLED = True
except:
        hasOLED = False

font1 = make_font("code2000.ttf",12)

try:

  if(hasOLED):
      with canvas(device) as draw:
         draw.text((5, 2), "PI Switch Cap Demo",font=font1, fill="white")
         draw.text((1, 18), "wlan0:" + GetWLANIP(),font=font1, fill="white")
         draw.text((1, 36), "eth0:" + GetLANIP(),font=font1, fill="white")

except:
  pass

raw_input("Showing IP address on OLED display. Press Enter to continue...")


