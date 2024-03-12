import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
import typing


def C5_func(q_grid: np.array, q_start: np.array, q_goal:np.array, c_path: typing.List[np.array]) -> typing.List[np.array]:
    """ Convert the path from indices of q_grid to actual robot configuraitons.

    Parameters
    ----------
    q_grid : np.array
        a numpy array representing the grid over the angle-range
    q_start : np.array
        a 2x1 numpy array representing the start configuration of the robot
    q_goal : np.array
         a 2x1 numpy array representing the goal configuration of the robot
    c_path : typing.List[np.array]
        a list of 2x1 numpy array representing the path from the start configuration to the goal configuration (indices of q_grid)

    Returns
    -------
    typing.List[np.array]
        a list of 2x1 numpy array representing the path from the start configuration to the goal configuration (actual angle values)
    """

    ### Insert your code below: ###
    q_path = [np.array([0,0]), np.array([0,0])]
    return q_path