from src.stats import *


class Character:
    def __init__(self, level, hit_dice, abilities, proficiencies, spellbase):
        self.level = level
        self.hit_dice = hit_dice
        self.abilities = abilities
        self.is_perceptive = "Perception" in proficiencies
        
        self.spellcasting = None
        
        if spellbase:
            self.spellcasting = Spellcasting(self, spellbase)

        self.checks = [
            # Saving Throws
            STRCheck(self, "STR ST"),
            DEXCheck(self, "DEX ST"),
            CONCheck(self, "CON ST"),
            INTCheck(self, "INT ST"),
            WISCheck(self, "WIS ST"),
            CHACheck(self, "CHA ST"),
            # Skills
            DEXCheck(self, "Acrobatics"),
            WISCheck(self, "Animal Handling"),
            INTCheck(self, "Arcana"),
            STRCheck(self, "Athletics"),
            CHACheck(self, "Deception"),
            INTCheck(self, "History"),
            WISCheck(self, "Insight"),
            CHACheck(self, "Intimidation"),
            INTCheck(self, "Investigation"),
            WISCheck(self, "Medicine"),
            INTCheck(self, "Nature"),
            WISCheck(self, "Perception"),
            CHACheck(self, "Performance"),
            CHACheck(self, "Persuasion"),
            INTCheck(self, "Religion"),
            DEXCheck(self, "Sleight of Hand"),
            DEXCheck(self, "Stealth"),
            WISCheck(self, "Survival")
        ]
        
        for check in self.checks:
            if check.name in proficiencies:
                check.is_proficient = True

    @property
    def xp(self):
        xp_by_level = [     0,    300,    900,   2700,   6500,
                        14000,  23000,  34000,  48000,  64000,
                        85000, 100000, 120000, 140000, 165000,
                       195000, 225000, 265000, 305000, 355000]
        
        return xp_by_level[self.level-1]

    @property
    def prof_bonus(self):
        return 2 + (self.level-1) // 4

    @property
    def passive_perception(self):
        passive = 10 + self.get_ability_mod("WIS")

        if self.is_perceptive:
            passive += self.prof_bonus
        
        return passive
    
    @property
    def hp(self):
        hp_average = (self.hit_dice // 2 + 1) * (self.level-1)
        hp_base = self.hit_dice + self.get_ability_mod("CON") * self.level
        
        hp_final = ""
        
        if self.level > 1:
            hp_final += f"({self.level-1}d{self.hit_dice}/{hp_average}) + "
        
        hp_final += str(hp_base)
        
        return hp_final

    def get_ability_mod(self, name):
        return (self.abilities[name] - 10) // 2
