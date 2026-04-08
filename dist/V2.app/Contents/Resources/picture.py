import pygame

screen = pygame.display.set_mode((400,400))
pygame.init()
img1 = pygame.image.load('aroom.png')
#img2 = pygame.image.load('whatever.png')
def makeText(text, color, bgcolor, top, left):
     # create the Surface and Rect objects for some text.
     textSurf = TEXT.render(text, True, color, bgcolor)
     textRect = textSurf.get_rect()
     textRect.topleft = (top, left)
     return (textSurf, textRect)
     textRect.width -= 19
     
TEXT = pygame.font.Font('freesansbold.ttf', 12)
size = 10
makeText('Nanomachines, son.',(127,127,127), (255,255,255), 10,30)
pygame.display.update()
