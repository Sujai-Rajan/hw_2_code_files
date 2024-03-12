import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
from q2poly import q2poly
import shapely
from shapely.geometry import Polygon as Polygon_shapely
from shapely import MultiPoint
import typing

from C1 import C1_func




def C6_func(robot: typing.Dict[str, typing.List[float]], q_path: typing.List[np.array], obstacles: typing.List[Polygon]) -> int:
    """Calculate the number of collisions that occur along the path.
    
    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    q_path : typing.List[np.array]
        A list of 2-element lists representing the path from the start configuration to the goal configuration (actual angle values)
    obstacles : typing.List[Polygon]
        A list of polygons representing the obstacles

    Returns
    -------
    int
        the number of collisions that occur along the path
    """

    ### Insert your code below: ###
    num_collisions = 0
    return num_collisions