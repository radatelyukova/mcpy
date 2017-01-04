#! /usr/bin/env python3
################################################################################
#   teleport.py
#
#   Teleportation 
#
#   03.01.2017  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

# Home
x_home = -18
y_home = 7
z_home = -28

mc.player.setTilePos(x_home,y_home,z_home)

# End of MC World
x = 30000000
y = 196
z = 29999800

time.sleep(3)
mc.player.setTilePos(x,y,z)

while (True):
    time.sleep(5)
    pos = mc.player.getTilePos()
    mc.postToChat('x='+str(pos.x)+'y ='+str(pos.y)+' z='+str(pos.z) )
    