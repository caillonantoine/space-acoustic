#coding:utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Solid(object):
    pass

class Wall(Solid):
    def __init__(self,eq,start,length):
        """Bi-dimensionnal"""
        self.eq = eq
        self.start = start
        self.length = length
        
def get_Wall_eq(start_point,end_point):
    """Bi-dimensionnal"""
    if start_point[0] == end_point[0]:
        return lambda x:(start_point[0],x)
    elif start_point[1] == end_point[1]:
        return lambda x:(x,start_point[1])
    else:
        a = (start_point[1] - end_point[1])/(start_point[0] - end_point[0])
        b = start_point[1] - a*start_point[0]
        return lambda x:(x,a*x+b)