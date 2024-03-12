import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
import typing


def C3_func(robot: typing.Dict[str, typing.List[float]], cspace: np.array,q_grid: np.array, q_goal: np.array) -> np.array:
    """Create a new 2D array that shows the distance from each point in the configuration space to the goal configuration.

    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    cspace : np.array
        The configuration space of the robot
    q_grid : np.array
        A numpy array representing the grid over the angle-range
    q_goal : np.array
        A 2x1 numpy array representing the goal configuration of the robot

    Returns
    -------
    np.array
       a 2D numpy array representing the distance from each cell in the configuration space to the goal configuration
    """

    ### Insert your code below: ###

    distances = cspace

    return distances