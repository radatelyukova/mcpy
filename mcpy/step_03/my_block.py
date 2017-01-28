#! /usr/bin/env python3
################################################################################
#   my_block.py
#
#   Blocks building
#
#   22.01.2017  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
time.sleep(10)

x=-7
y=6
z=-26

#block_type = 57
#
#for i in range(0,11):
#    mc.setBlock(x, y+i, z, block_type)
    
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

width  = 8
height = 5
length = 6 

block_type = 47
mc.setBlocks(x, y, z, x + width, y + height, z + length, block_type)

block_type = 0
mc.setBlocks(x+1, y+1, z+1, x + width-1, y + height-1, z + length-1, block_type)
