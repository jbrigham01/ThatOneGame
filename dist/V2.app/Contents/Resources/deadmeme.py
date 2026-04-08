import pygame

screen = pygame.display.set_mode((800,800))
pygame.init()
img1 = pygame.image.load('aroom.png')
#img2 = pygame.image.load('whatever.png')
def makeText(text, color, bgcolor, top, left):
     textobj = pygame.font.Font('/usr/share/fonts/truetype/freefont/FreeSans.ttf',20)
     # create the Surface and Rect objects for some text.
     textSurf = textobj.render(text, True, color, bgcolor)
     textRect = textSurf.get_rect()
     textRect.topleft = (top, left)
     screen.blit(textSurf,textRect)
     return (textSurf, textRect)
     


makeText('Nanomachines, son.', (255,255,255),(127,127,127),350,400)
pygame.display.update()
