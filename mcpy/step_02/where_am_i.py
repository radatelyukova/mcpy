################################################################################
#   where_am_i.py
#
#   <Module for MC Purpose>
#
#   30.12.2016  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while (True):
    time.sleep(2)
    pos = mc.player.getTilePos()
    
    print("x="+str(pos.x) +" y="+str(pos.y) +" z="+str(pos.z))
    mc.postToChat("x="+str(pos.x) +" y ="+str(pos.y) + " z ="+str(pos.z))
