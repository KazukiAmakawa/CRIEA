############################################################
#
#		Random Walk Image Edge Alorithm
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Main.py
#
############################################################

#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from scipy import signal
from collections import deque
from PIL import ImageFilter
import cv2
from copy import deepcopy
import random

#import Files
import Init
import Constant
import Pretreatment
import Algorithm
DEBUG = Constant.DEBUG

def Main():
	"""
	#==============================================================================
	#Initial
	#==============================================================================
	"""
	if DEBUG:
		print("Pretreatment")

	img = np.array(Image.open(Constant.ImageName).convert("L"))



	"""
	#==============================================================================
	#Toboggan Algorithm
	#==============================================================================
	"""
	TobImg, TobBlock = Algorithm.Toboggan(img)




	"""
	#==============================================================================
	#Get the seed pixels
	#==============================================================================
	"""
	Seed = Algorithm.GetSeed(img)
	TobSeed = []
	for i in range(0, len(Seed)):
		TobBlock[i][0] = 0
		TobSeed.append(TobImg[Seed[i][0]][Seed[i][1]])



	"""
	#==============================================================================
	#Build Probability Matirx
	#==============================================================================
	"""
	if DEBUG:
		print("Main Calculation")
	ProbArr = Algorithm.ProbCal(TobBlock, TobSeed)
	if DEBUG:
		Init.ArrOutput(ProbArr)



	"""
	#==============================================================================
	#Decision
	#==============================================================================
	"""
	if DEBUG:
		print("Decision Part")
	









Main()
