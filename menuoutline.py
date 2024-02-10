class player:
    def __init__(self,name,level,inventory,Mhealth,Chealth,Mmagic, Cmagic,attack,defense,speed):
        self.name = name
        self.inventory = inventory
        self.Mhealth = Mhealth
        self.Chealth = Chealth
        self.Mmagic = Mmagic
        self.Cmagic = Cmagic
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    def drink_hprestore(self):
        if self.inventory['HPrestore'] <= 0:
            print("You can't drink what you don't have!")
            self.OpenMenu()
        else:
            self.Chealth = self.Chealth + (self.Mhealth/2)
            self.inventory['HPrestore'] -= 1
    def drink_mprestore(self):
        if self.inventory['MPrestore'] <= 0:
            print('Really, now.')
            self.OpenMenu()
        else:
            self.Cmagic = self.Mmagic
            self.inventory['MPrestore'] -= 1
    def OpenMenu(self):
        print('What would you like to do?')
        print('You have '+str(self.Chealth)+' health and '+str(self.Cmagic)+' magic.')
        print('Items, save, exit')
        choice = input()
        if 'items' in choice.lower():
            print('What would you like to consume?')
            print('HPrestore, MPRestore')
            choice2 = input()
            if 'hprestore' in choice2.lower():
                self.drink_hprestore()
                self.OpenMenu()
            elif 'mprestore' in choice2.lower():
                self.drink_mprestore()
                self.OpenMenu()
            else:
                print('You had one job. ONE. JOB.')
                OpenMenu(self)
        if 'save' in choice.lower():
            print("I haven't made a save function, yet. :\\")
            self.OpenMenu()
        if 'whatdoihave' in choice.lower():
            print(self.inventory)
            self.OpenMenu()
        else:
            print('You need to learn to read.')
            self.OpenMenu()
jeff = player('jeff', 14, {'Gold' : 100, 'HPrestore' : 2, 'MPrestore' : 2}, 100,20,50,10,100,100,13)

jeff.OpenMenu()
                    
    
    
        