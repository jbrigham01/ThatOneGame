import time
import random
import sys
global winner
global loser
from playerconstants import *
def Youlose():
    print('The battle was lost...')
    yorn = input('do you want to try again?')
    if 'y' in yorn:
        battlestart(Fredrick,mook)
    else:
        sys.exit()

def Youwin():
    print('You won the battle!')
    print('cool.')
    print('press ctrl-d to leave!')
    print('Or, do you want to try again?')
    tryagain = input('type your answer!')
    if 'y' in tryagain:
        battlestart(Fredrick, mook)
    else:
        sys.exit()
    
            

   
def playerturn(PLAYER, enemy):
    PLAYER.block = False
    command = input('what do you want to do? You can ATTACK, DEFEND, or MAGIC.  ')
    if command.lower() == 'attack':
        attackwhom = input('attack who?  ')
        if attackwhom == enemy.name:
            PLAYER.physicalattack(enemy)
        else:
            print('that is not an option.')
            playerturn(PLAYER, enemy)
    elif command.lower() == 'defend':
        PLAYER.block = True
        print('Damage taken will be reduced!')
    elif command.lower() == 'magic':
        print('Known spells : '+str(PLAYER.spells)+'.')
        mtype = input('What kind of magic?')
        if 'holy' in mtype:
            PLAYER.magicattack(holy, enemy)
        
    if enemy.currenthealth <= 0:
        Youwin()
            
         
        
    

class enemy:
    def __init__(self,name,maxhealth,currenthealth, attack, defense, speed, block):
        self.name = name
        self.maxhealth = maxhealth
        self.currenthealth = currenthealth
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.block = False
    def attackplayer(self, PLAYER):
        PLAYER.currenthealth -= self.attack
    def enemyturn(self, PLAYER):
        print('The enemy does an attack thingy!')
        if PLAYER.block:    
            damage= (self.attack- PLAYER.defense)/2
        elif not PLAYER.block:
            damage = (self.attack - PLAYER.defense)
        PLAYER.Chealth -= damage
        print('You took '+str(damage)+ ' damage!')
        print('The enemy blocks for testing purposes!')
        self.block = True
        if PLAYER.Chealth <= 0:
            Youlose()
  
            
       


def battleloop(PLAYER,enemy):
    while True:
        if PLAYER.Chealth == 0:
            Youlose()
        elif enemy.currenthealth <= 0:
            Youwin()
        print('playerhealth = ' +str(PLAYER.Chealth))
        print('playermagic = ' +str(PLAYER.Cmp))
        print('enemyhealth = ' + str(enemy.currenthealth))
        playerturn(PLAYER,enemy)
        enemy.enemyturn(PLAYER)
     
  
def battlestart(PLAYER, enemy):
    global winner
    global loser
    winner = False
    loser = False
    PLAYER.Chealth = PLAYER.Mhealth
    enemy.currenthealth = enemy.maxhealth
    print("You engage the " +enemy.name+ '.')   
    if PLAYER.speed > enemy.speed:
        print('You attack first!')
        #player's turn starts now
        PLAYER.playerturn(enemy)
        PlayerHeadStart = 1
        battleloop(player, enemy)
                                
    elif PLAYER.speed < enemy.speed:
        print('The enemy attacks first.')
        enemy.enemyturn(PLAYER)
        EnemyHeadstart = 1
        battleloop(PLAYER, enemy)
    elif PLAYER.speed == enemy.speed:
        print('Random deciding who attacks first.')
        wgf = random.randint(1,2)
        if wgf == 2:
            PLAYER.playerturn(enemy)
            PlayerHeadstart = 1
            battleloop(player, enemy)
        elif wgf == 1:
            enemy.enemyturn(PLAYER)
            EnemyHeadstart = 1
            battleloop(player, enemy)
    
    

Fredrick = Player('Fredrick', '1', None, 'beta tester', 1,100, 100, 50, 50, 15, 10, 5, 10, ['holy'])

mook = enemy('mook',100,100,20,20,9,False)

battlestart(Fredrick,mook)
    
    
