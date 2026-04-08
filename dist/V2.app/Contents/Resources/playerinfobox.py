import playerconstants
from playerconstants import Fredrick
import time
import sys
import pygame

pygame.init()
class Playerinfobox:
    def __init__(self, player, location):
        self.player = player
        self.location = location
        self.rect = pygame.rect.Rect(300, 425, 100,75)
        self.image2 = pygame.image.load('playerstatusbox.png')
        self.Mhealth = player.Mhealth
        self.Chealth = player.Chealth
        self.Mmp = player.Mmp
        self.Cmp = player.Cmp
        self.status = None
        self.image = player.statusboximage

Finfo = Playerinfobox(Fredrick, (300,250))

Hobj = pygame.font.Font(None, 18)
htso = Hobj.render(str(Finfo.Chealth)+'/'+str(Finfo.Mhealth)+'HP', True, (0,0,0), None)
htro = htso.get_rect()
htro.center = (45,20)

Mobj = pygame.font.Font(None, 18)
Mtso = Mobj.render(str(Finfo.Cmp)+'/'+str(Finfo.Mmp)+'MP', True, (0,0,0), None)
mtro = Mtso.get_rect()
mtro.center = (45,40)  
def displaystatusbox(player, distname):
    distname.blit(Finfo.image2, Finfo.rect)
    distname.blit(htso, (Finfo.rect.centerx-10, Finfo.rect.centery-20))
    distname.blit(Mtso, (Finfo.rect.centerx-10,Finfo.rect.centery))
    distname.blit(Finfo.image, Finfo.rect.topleft)

    
    
        




        

