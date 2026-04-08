import time
import pygame
import copy
import sys
pygame.init()
fpr = pygame.time.Clock()
cursor = pygame.mixer.Sound('cursor.wav')
cursorcleaner = pygame.image.load('cursorcleaner.png')
screen= pygame.display.set_mode((600, 500))
pygame.display.set_caption('choicetest')
class textbox:
    def __init__(self, rect, image):
        self.rect = pygame.rect.Rect(rect)
        self.image = pygame.image.load(image)
text = textbox((50,350,400,00), 'textbox.png')
class choicepointer:
    def __init__(self,rect,image, currentloc=0):
        self.rect = pygame.rect.Rect(rect)
        self.image = pygame.image.load(image)
        self.currentloc = currentloc
pointer = choicepointer((text.rect.topleft[0],300,15,15),'pointer.png')
    
def askandquestion(moo, pointer,choice1, choice2):
    answergiven = False
    maxlist = len(moo)
    currentlist = 0
    screen.blit(text.image, text.rect)
    # No more than 75 characters, okay?
    for y in range(1,maxlist-1):
        z = moo[y]
        font = pygame.font.Font(None,20)
        tso = font.render(z, True, (0,0,0), (255,255,255))
        tro = tso.get_rect()
        # how to change distance so that it is not one blob of letters?
        tro.center = (text.rect.topleft[0] + (y*10) + 15 , text.rect.topleft[1] + 20)
        if y >= 38:
            tro.centery += 20
            tro.centerx -= 370
        if y >= 75:
            tro.centery += 20
            tro.centerx -= 370
        
        
        screen.blit(tso,tro)
        if z != ' ':
            cursor.play()
        pygame.display.update()
        currentlist += 1
        if z == '.':
            time.sleep(0.5)
        if z == ',':
            time.sleep(0.25)
        else:
            time.sleep(0.03)
    q1 = font.render(choice1, True, (0,0,0), (255,255,255))
    qro1 = q1.get_rect()
    qro1.center = (text.rect.topleft[0] + 70, text.rect.topleft[1] + 70)
    screen.blit(q1, qro1)
    pygame.display.update()
    time.sleep(0.5)
    q2 = font.render(choice2, True, (0,0,0), (255,255,255))
    qro2 = q2.get_rect()
    qro2.center = (text.rect.topleft[0] + 250, text.rect.topleft[1] + 70)
    screen.blit(q2,qro2)
    pygame.display.update()        
    time.sleep(1)
    
    rightcheck = None
    leftcheck = None 
    while not answergiven:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rightcheck = 1
                if event.key == pygame.K_LEFT:
                    leftcheck = 1
                if event.key == pygame.K_z:
                    print('Triggered')
                    zcheck = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and rightcheck == 1:
                    pointer.currentloc += 1
                    rightcheck = 0
                    if pointer.currentloc >= 2:
                        pointer.currentloc = 0
                if event.key == pygame.K_LEFT and leftcheck == 1:
                    leftcheck = 0
                    pointer.currentloc -= 1
                    if pointer.currentloc <= -1:
                        pointer.currentloc = 1
                if event.key == pygame.K_z and zcheck == 1:
                    print('Should go through')
                    zcheck = 0
                    if pointer.currentloc == 0:
                        chosenoption = choice1
                    else:
                        chosenoption = choice2
                    
                    answergiven = True
                    
            try:
                if pointer.currentloc != lastcurrentloc:
                    screen.blit(cursorcleaner, lastcursor)
            except UnboundLocalError:
                pass
            

                
            pointer.rect.center = (text.rect.topleft[0] + (40 if pointer.currentloc == 0 else 235),
                                   text.rect.topleft[1] + 70)
            lastcursor = copy.copy(pointer.rect)
            lastcurrentloc = copy.copy(pointer.currentloc)
            
                
            screen.blit(pointer.image, pointer.rect)
            pygame.display.update()
    else:
        print(chosenoption + 'was chosen')
        answergiven = True
        return chosenoption
    return chosenoption

    
            
                    
                    
        
        
while True:
    askandquestion('\' Did this work? ', pointer,'Yes','No')
    print(chosenoption)
    pygame.quit()
    sys.exit()
