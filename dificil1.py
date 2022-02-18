import pygame
from Sudoku import solve, valid
import time
from pygame import *
pygame.font.init()


class Grid:
    # To change the starting board change this
    board = [
        [5,
