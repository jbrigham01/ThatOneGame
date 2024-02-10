import pygame
import sys
from pygame.locals import *

surface = pygame.display.set_mode((400,400))
pygame.display.set_caption('battle system')

# Let's map out what we want it to do
""" Like MMBN and TOTA had a baby. And it was good.
The battle system should have a bunch of squares in a 8x4 format, for now.
Characters should move on their side.
"""
