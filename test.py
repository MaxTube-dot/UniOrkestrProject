import os
import copy
from model import *
import random
import shutil


defect = Defect(1, 220, 283)
data = defect.get_opposite_points(960, 600)

rtr = 1