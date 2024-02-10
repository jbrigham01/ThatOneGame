import pygame
import sys
import time
from playerconstants import PLAYER, Fredrick
class party:
    def __init__(self,member1,member2,member3,member4):
        self.member1 = member1
        self.member2 = member2
        self.member3 = member3
        self.member4 = member4
        self.members = [member1,member2,member3,member4]

currentparty = party(Fredrick,None,None,None)
print(currentparty.members)
