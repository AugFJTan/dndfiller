class SkillCheck:
    def __init__(self, character, name, base):
        self.character = character
        self.name = name
        self.base = base
        self.is_proficient = False

    @property
    def score(self):
        score = self.character.get_ability_mod(self.base)
        if self.is_proficient:
            score += self.character.prof_bonus
        return score


class STRCheck(SkillCheck):
    def __init__(self, character, name):
        super().__init__(character, name, "STR")


class DEXCheck(SkillCheck):
    def __init__(self, character, name):
        super().__init__(character, name, "DEX")


class CONCheck(SkillCheck):
    def __init__(self, character, name):
        super().__init__(character, name, "CON")


class INTCheck(SkillCheck):
    def __init__(self, character, name):
        super().__init__(character, name, "INT")


class WISCheck(SkillCheck):
    def __init__(self, character, name):
        super().__init__(character, name, "WIS")


class CHACheck(SkillCheck):
    def __init__(self, character, name):
        super().__init__(character, name, "CHA")


class Spellcasting:
    def __init__(self, character, base):
        self.character = character
        self.base = base

    @property
    def save_DC(self):
        return 8 + self.total_spell_mod()

    @property
    def attack(self):
        return self.total_spell_mod()

    def total_spell_mod(self):
        spell_mod = self.character.get_ability_mod(self.base)
        return self.character.prof_bonus + spell_mod
