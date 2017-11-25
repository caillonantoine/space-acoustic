#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

class Solid(object):
    pass
    
class Wall(Solid):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def get_collision_instant(self,x0,t0,cd):
        