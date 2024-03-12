import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *

def C7_func(cspace: np.array) -> np.array:
    """Pad the configuration space by one grid cell.

    Parameters
    ----------
    cspace : np.array
        The origianl configuration space of the robot

    Returns
    -------
    np.array
        The padded configuration space of the robot
    """

    ### Insert your code below: ###
    padded_cspace = cspace.copy()
    
    return padded_cspace