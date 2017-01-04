################################################################################
#   hello.py
#
#   <Module for MC Purpose>
#
#   30.00.2016  Created by: Rada Telyukova
################################################################################

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
time.sleep(5)
mc.postToChat("Hello Minecraft!!")
