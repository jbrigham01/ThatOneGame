import pygame
import sys
from pygame.locals import *
from playerconstants import Fredrick
import time

display = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Battle System, GO!')
pygame.init()
# This has to be written because the previous battlesystem was destroyed due to my computer
# I hate you, computer.
# Like MMBN, 6x3 grid is where battles are conducted. Half for player, Half for enemy.
# However, Players and enemys can get up close and personal, or attack
# from a distance, as there are no boundaries, like Tales games
class battletile:
    def __init__(self, coords, state,owner):
        self.coords = coords # like [1,1], [2.3], etc. Not 100, 200.
        self.rect = pygame.Rect(self.coords[0] *100 - 100, (self.coords[1] * 100) , 100, 100)
        self.state = state
        self.image = None #Not yet...
        self.owner = owner
        self.occupied = None
        
        self.playerisonit = None
        # add more later...
    def tilechange(self):
        if self.state == 'normal':
            self.image = pygame.image.load('grasstile.png')
        if self.state == 'broken':
            self.image = pygame.image.load('brokentile.png')
        if self.state == 'poison':
            self.image = pygame.image.load('poisontile.png')
ab = 'normal'
bb = 'player'
cb = 'enemy'
a = battletile([1,1],ab,bb)
b = battletile([1,2],ab,bb)
c = battletile([1,3],ab,bb)
d = battletile([2,1],ab,bb)
e = battletile([2,2],ab,bb)
f = battletile([2,3],ab,bb)
g = battletile([3,1],ab,bb)
h = battletile([3,2],ab,bb)
i = battletile([3,3],ab,bb)
j = battletile([4,1],ab,cb)
k = battletile([4,2],ab,cb)
l = battletile([4,3],ab,cb)
m = battletile([5,1],ab,cb)
n = battletile([5,2],ab,cb)
o = battletile([5,3],ab,cb)
p = battletile([6,1],ab,cb)
q = battletile([6,2],ab,cb)
r = battletile([6,3],ab,cb)
alltiles = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r)
def blitbattlearea():
    for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        x.tilechange()
        display.blit(x.image, x.rect)


class battleplayer:
    def __init__ (self,startpoint,name):
#        self.inheritsfrom = inheritsfrom
        self.startpoint = [2,2]
        self.currentpos = startpoint
        self.battlesprite = pygame.image.load('Fbattlesprite.png')
        self.name = name
        self.Mhealth = Fredrick.Mhealth
        self.Chealth = Fredrick.Chealth
        self.Mmp = Fredrick.Mmp
        self.Cmp = Fredrick.Cmp
        self.attack = Fredrick.attack
        self.defense = Fredrick.defense
        self.magic = Fredrick.magic
        self.speed = Fredrick.speed
        self.isonpoison = None

class enemy:
    def __init__(self,startpoint, name,level, battlesprite, Mhealth, Chealth, Mmp,
                 Cmp, attack, defense, magic, speed, strategy):
        self.startpoint = [5,2]
        self.currentpos = startpoint
        self.name = name
        self.level = level
        self.battlesprite = pygame.image.load(battlesprite)
        self.Mhealth = Mhealth
        self.Chealth = Chealth
        self.Mmp = Mmp
        self.Cmp = Cmp
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        self.strategy = strategy
        self.battlecounter = 0
        self.statusboximage = pygame.image.load('Gstatusboxsprite.png')
ghostface = enemy([5,2], 'Ghostface', 10, 'Gbattlesprite.png', 500, 500, 100, 100,
                  50,30,50,14,1)
def strategy(self):
    self.battlecounter += 1
    if self.battlecounter % 10 == 0:
        if fredrick.currentpos[1] == self.currentpos[1]:
            for x in alltiles:
                if x.coords[1] == self.currentpos[1]:
                    if x.playerisonit == True:
                        fredrick.Chealth -= 10    
        if fredrick.currentpos[1] == 1:
            self.currentpos[1] -=1
            for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    if (x.state == 'broken' or x.occupied == True or x.playerisonit == True) and self.currentpos == x.coords:
                        self.currentpos[1] += 1
            if self.currentpos[1]<=0:
                self.currentpos[1] = 1
        elif fredrick.currentpos[1] == 3:
            self.currentpos[1] += 1
            for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    if (x.state == 'broken' or x.occupied == True or x.playerisonit == True) and self.currentpos == x.coords:
                        self.currentpos[1] -= 1
            if self.currentpos[1] >= 4:
                self.currentpos[1] = 3
        
def getlocation(self):
    for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
            if self.currentpos == x.coords and x.state != 'broken':
                return (x.rect.centerx-25, x.rect.centery-50)
           
fredrick = battleplayer([2,2], 'Fredrick')

class Playerinfobox:
    def __init__(self, player, location):
        self.player = player
        self.location = location
        self.rect = pygame.rect.Rect(200, 425, 100,75)
        self.image2 = pygame.image.load('playerstatusbox.png')
        self.Mhealth = player.Mhealth
        self.Chealth = player.Chealth
        self.Mmp = player.Mmp
        self.Cmp = player.Cmp
        self.status = None
        self.image = player.statusboximage

class Enemyinfobox:
    def __init__(self, enemy, location):
        self.enemy = enemy
        self.location = location
        self.rect = pygame.rect.Rect(300, 425, 100,75)
        self.image2 = pygame.image.load('playerstatusbox.png')
        self.Mhealth = enemy.Mhealth
        self.Chealth = enemy.Chealth
        self.Mmp = enemy.Mmp
        self.Cmp = enemy.Cmp
        self.status = None
        self.image = enemy.statusboximage
def epoisoncheck():
    if e.state == 'poison' and e.playerisonit == True:
        fredrick.isonpoison = True
    else:
        fredrick.isonpoison = False
def displaystatusbox():
    Finfo = Playerinfobox(Fredrick, (300,250))
   
    Hobj = pygame.font.Font(None, 16)
    htso = Hobj.render(str(fredrick.Chealth)+'/'+str(fredrick.Mhealth)+'HP', True, (0,0,0), None)
    htro = htso.get_rect()
    htro.center = (45,20)


    Mobj = pygame.font.Font(None, 16)
    Mtso = Mobj.render(str(fredrick.Cmp)+'/'+str(fredrick.Mmp)+'MP', True, (0,0,0), None)
    mtro = Mtso.get_rect()
    mtro.center = (45,40)
    display.blit(Finfo.image2, Finfo.rect)
    display.blit(htso, (Finfo.rect.centerx-10, Finfo.rect.centery-20))
    display.blit(Mtso, (Finfo.rect.centerx-10,Finfo.rect.centery))
    display.blit(Finfo.image, Finfo.rect.topleft)


def displayenemystatusbox():
    Ginfo = Enemyinfobox(ghostface, (400,250))
    GHobj = pygame.font.Font(None, 16)
    Ghtso = GHobj.render(str(ghostface.Chealth)+'/'+str(ghostface.Mhealth)+'Hp', True, (0,0,0), None)
    Gtro = Ghtso.get_rect()
    Gtro.center = (45,20)
    display.blit(Ginfo.image2, Ginfo.rect)
    display.blit(Ghtso, Ginfo.rect.center)
    display.blit(Ginfo.image, Ginfo.rect.topleft)
xcounter = 0
while True:
    if fredrick.isonpoison == True:
        xcounter = xcounter + 1
        if xcounter == 10:
            fredrick.Chealth -= 1
            xcounter = 0
    fps = pygame.time.Clock()
    display.fill((255,255,255))
    blitbattlearea()
    display.blit(fredrick.battlesprite, getlocation(fredrick))
    display.blit(ghostface.battlesprite, getlocation(ghostface))
    displaystatusbox()
    displayenemystatusbox()
    strategy(ghostface)
    for event in pygame.event.get():
        if event.type == QUIT:    
                pygame.quit()
                sys.exit() 
        if event.type == KEYDOWN:
            
            if event.key == K_UP:
                fredrick.currentpos[1] -= 1
                if fredrick.currentpos[1] <= 0:
                    fredrick.currentpos[1] = 1
                for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    if (x.state == 'broken' or x.occupied == True) and fredrick.currentpos == x.coords:
                        fredrick.currentpos[1] += 1
               
            if event.key == K_DOWN:
               fredrick. currentpos[1] += 1
               if fredrick.currentpos[1] >= 4:
                    fredrick.currentpos[1] = 3
               for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    if (x.state == 'broken' or x.occupied == True) and fredrick.currentpos == x.coords:
                        fredrick.currentpos[1] -= 1
 
            if event.key == K_LEFT:
                fredrick.currentpos[0] -= 1
                if fredrick.currentpos[0] <= 0:
                    fredrick.currentpos[0] = 1
                for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    if (x.state == 'broken' or x.occupied == True) and fredrick.currentpos == x.coords:
                        fredrick.currentpos[0] += 1

            if event.key == K_RIGHT:
                fredrick.currentpos[0] += 1
                if fredrick.currentpos[0] >= 7:
                    fredrick.currentpos[0] = 6
                for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    if (x.state == 'broken' or x.occupied == True) and fredrick.currentpos == x.coords:
                       fredrick.currentpos[0] -= 1

            if event.key == K_z:
                for x in (a,c,e,g,i,j,l,m,p,r):
                    x.state = 'broken'
                    if (x.occupied == True or x.playerisonit == True) and x.state == 'broken':
                        x.state = 'normal'
            if event.key == K_x:
                for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
                    x.state = 'normal'
            if event.key == K_c:
                e.state = 'poison'
            lastloc = fredrick.currentpos
    for x in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        if fredrick.currentpos == x.coords:
            x.playerisonit = True
        if ghostface.currentpos == x.coords:
            x.occupied = True
        if fredrick.currentpos != x.coords:
            x.playerisonit = False
        if ghostface.currentpos != x.coords:
            x.occupied = False
    if e.state == 'poison' and e.playerisonit == 'True':
        fredrick.isonpoison = True
    epoisoncheck()
    print(fredrick.isonpoison)       
    print('Player position is:'+str(fredrick.currentpos))
    print('Enemy position is:'+str(ghostface.currentpos))
    pygame.display.update()
    fps.tick(30)
    
    
            

