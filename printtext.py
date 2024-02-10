import pygame
import sys
from pygame.locals import *
import time
pygame.init()
DISPLAY = pygame.display.set_mode((550,500
                                   ))
pygame.display.set_caption('print things')
moo = 'What a polite young man she was..?'
fps = pygame.time.Clock()
class textbox:
    def __init__(self, rect, image):
        self.rect = pygame.rect.Rect(rect)
        self.image = pygame.image.load(image)
text = textbox((0,100,400,00), 'textbox.png')
        
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
##def talkprint(text):
##    maxlist = len(text)
##    currentlist = 0
##    while currentlist < maxlist:
##        for y in range(0,maxlist-1):
##            z = text[y]
##            font = pygame.font.Font(None,16)
##            tso = font.render(z, True, (0,0,0), WHITE)
##            tro = tso.get_rect()
##            tro.center = (y*10, 150)
##            DISPLAY.blit(tso,tro)
##            currentlist += 1
##            time.sleep(0.01)
##            
fontObj = pygame.font.Font(None, 22)
textSurfaceObj = fontObj.render('Do you wanna buy a stick', True, GREEN, BLUE)
textRectObj = pygame.rect.Rect(0,400,0,100)
textRectObj.center = (200,150)
mooz = 0
cursor = pygame.mixer.Sound('cursor.wav')
def printstuff(moo):
    maxlist = len(moo)
    currentlist = 0
    DISPLAY.blit(text.image, text.rect)
    while currentlist < maxlist:
        for y in range(0,maxlist):
            z = moo[y]
            font = pygame.font.Font(None,20)
            tso = font.render(z, True, (0,0,0), WHITE)
            tro = tso.get_rect()
            # how to change distance so that it is not one blob of letters?
            tro.center = ((y*10) + 15 , text.rect.topleft[1] + 20)
            if y >= 38:
                tro.centery += 20
                tro.centerx -= 380
            DISPLAY.blit(tso,tro)
            cursor.play()
            pygame.display.update()
            currentlist += 1
            #if y < 22:
            time.sleep(0.1)

           # else:
            #    time.sleep(1)
        print('finished!')
while mooz < 1:
    print('taco')
    DISPLAY.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    printstuff(moo)
    break


