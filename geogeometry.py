import numpy as np
import pylab as plt
import itertools
from scipy import stats

from shapely.geometry import Point, Polygon, LineString, MultiPolygon


def count_intersections(N=2):
    """This function counts the number of intersections from the randomly
       drawn lines

    Args:
        N (int, optional): number of lines drawn. Defaults to 2.

    Returns:
        len(xx): number of intersections
        xx: intersections
        lines: randomly drawn lines
    """
    
    #N = 10
    lines = []
    for _ in range(int(N/2)):
        line_h = LineString([(np.random.random()*10,0),(np.random.random()*10,10)])
        line_v = LineString([(np.random.random()*10,0),(np.random.random()*10,10)])
        lines.append(line_h) # horizontal
        lines.append(line_v) # vertical
    combos = itertools.combinations(lines, 2)
    intersections = []
    for seg in combos:
        x = seg[0].intersection(seg[1])
        intersections.append(x)
    xx = [x.coords[:][0] for x in intersections if x.is_empty is False]
    return len(xx), xx, lines


def count_mosaics(max_lines):
    """This function counts the mosaics created from the randomly drawn
       lines

    Args:
        max_lines ([type]): maximum number of lines to draw; used in loop

    Returns:
        global_mosaics_pass [type]: mosaics created from all loops
        global_mosaics_size []: number of mosaics created as function of
                                the number of lines drawn
    """

    global_mosaics_pass = [] # array for all passed mosaics
    global_mosaics_size = [] # array for all passed mosaics sizes
    for num in range(3,max_lines+1):
        intersections_count, intersections, lines = count_intersections(num)
        mosaics  = []
        for NN in range(3,intersections_count+1):
            mosaics.extend(itertools.combinations(intersections, NN))
        mosaics = [mosaic for mosaic in mosaics if Polygon(mosaic).is_valid]  
        
        # remove mosaic if it intersects with any of the lines
        # count number of points/nodes for remaining mosaics 
        local_mosaics_pass = []
        local_mosaics_size = []
        for mosaic in mosaics:
            tst = []
            for line in lines:
                tst.append(line.within(Polygon(mosaic)))
            if not sum(tst*1):
                local_mosaics_pass.append(mosaic)
                local_mosaics_size.append(len(mosaic))
    global_mosaics_pass.append([local_mosaics_pass])
    global_mosaics_size.append([local_mosaics_size])
    
    return global_mosaics_pass, global_mosaics_size