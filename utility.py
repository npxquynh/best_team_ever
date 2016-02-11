from __future__ import division
import math

def cal_distance(x1, y1, x2, y2):
    return round(math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)), 0)