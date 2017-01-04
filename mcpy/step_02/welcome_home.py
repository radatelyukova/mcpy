#! /usr/bin/env python3
################################################################################
#   welcome_home.py
#
#   <Executable Module for MC Purpose>
#
#   29.12.2016  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x_home = -18
y_home = 7
z_home = -28
mc.postToChat("x="+str(pos.x) +" y ="+str(pos.y) + " z ="+str(pos.z))
while (True):
    time.sleep(2)
    pos = mc.player.getTilePos()

    if (pos.x == x_home and pos.y == y_home and   pos.z == z_home):
        mc.postToChat('Welcome home!')
    