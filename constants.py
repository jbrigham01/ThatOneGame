class PLAYER:
    def __init__(self, name, level, statuseffect,  title,Mhealth, Chealth, Mmp, Cmp, attack, defense, speed, magic, Sdefense, spells, specials):
        self.name = name
        self.level = level
        self.title = title
        self.Mhealth = Mhealth
        self.Chealth = Chealth
        self.Cmp = Cmp
        self.Mmp = Mmp
        self.attack = 10 + (int(level) * 4)
        self.defense = 10 + (int(level) * 2)
        self.speed = 4 +(int(level)*1)
        self.magic = 10 + (int(level) * 4)
        self.Sdefense = 5 + (int(level) * 2)
        self.spells = spells
        self.specials = spells
        self.block = False
    
    def physicalattack(self,enemy):
        cdamage = random.randint(self.attack*2, self.attack*2.5)
        if enemy.block:
            enemy.chealth -= cdamage/2
        elif not enemy.guard:
            enemy.chealth -= cdamage
    def magicattack(self,spell, enemy):
        cdamage = self.magic * spell.basedamage
        if enemy.block:
            enemy.health -= cdamage/2
        elif not enemy.shell:
            enemy.health -= cdamage
    def block(self):
        print('Damage taken will be halved!')
        self.block = True
    class spell:
        def __init__(self, name,basedamage, element, mpcost, effect):
            self.name = name
            self.basedamage = basedamage
            self.element = element
            self.mpcost = mpcost
            self.effect = effect
        
    def specials(spell):
        self.mpcost = None
        self.damage = player.attack * self.basedamage
class ENEMY(PLAYER):
    def __init__(resist, weakness, strategy):
    #maybe later
        self.resist = resist
holy = PLAYER.spell('Holy', 25, 'Light', 25, None) 
Fredrick = PLAYER('Fredrick', '1', None, 'beta tester', 100, 100, 50, 50, 15, 10, 5, 10, 10, [holy],[])
