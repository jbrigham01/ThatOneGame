import pygame
import sys
display = pygame.display.set_mode((400,400))
class player(pygame.sprite.Sprite):
    def __init__(self, location, orientation, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('sprites/player.png')
        self.imageDefault = self.image.copy()# Actual size is 28x56
        self.rect = pygame.Rect(location, (30,60))
        self.orient = orientation 
        self.holdTime = 0
        self.walking = False
        self.dx = 0
        self.step = 'rightFoot'
Player = player('1', '1')
while True:
    display.blit(Player.image, Player.rect)
    time.sleep(1)
    Player.image.scroll(30,0)
    time.sleep(1)
    Player.image.scroll(60,0)
