import sys
from .utils import Color, colorprint



def fatal_error(message):
    """
    print error message with color red and exit program
    """
    colorprint(message, Color.RED)
    exit()