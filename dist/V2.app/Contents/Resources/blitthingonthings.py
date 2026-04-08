import pygame
x = 0
y = 0
screen = pygame.display.set_mode([800,800], 0, 32)

img1 = pygame.image.load('aroom.png')
moo = (0,0,2,2)
img2 = pygame.image.load('blackcloak.png').convert_alpha()
screen.fill([0,0,0])
screen.blit(img1, moo)
screen.blit(img1, [200,200])
img1.blit(img2, [x,y])
pygame.display.update()

##while True:
##    key = pygame.key.get_pressed()
##    for event in pygame.event.get():
##            if key[pygame.K_LEFT]:
##                direction = 'left'
##                x = x - 50
##                if x < 0:
##                    x = 0
##            elif key[pygame.K_RIGHT]:
##                direction = 'right'
##                x = x + 50
##            elif key[pygame.K_DOWN]:
##                direction = 'down'
##                y = y - 50
##                if y < 0:
##                    y = 0
##            elif key[pygame.K_UP]:
##                direction = 'up'
##                y = y + 50
##            elif event.type == QUIT:
##                pygame.quit()
##                sys.exit()

    
pygame.display.update()
    

