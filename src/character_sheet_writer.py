import json
from fillpdf import fillpdfs


class CharacterSheetWriter:
    def __init__(self, character):
        self.character = character
        self.output = {}
        
        with open('form-fields.json') as file:
            self.fields = json.load(file)

    def write_to_PDF(self, input_file, output_file):
        self.set_abilites()
        self.set_proficiencies()
        self.set_spellcasting()
        self.set_miscellaneous()
        
        fillpdfs.write_fillable_pdf(input_file, output_file, self.output)

    def set_abilites(self):
        for stat, value in self.character.abilities.items():
            mod = self.character.get_ability_mod(stat)

            if mod >= 0:
                mod_display = f"+{mod}"
            else:
                mod_display = str(mod)

            self.set_value(stat, str(value))
            self.set_value(f"{stat} Mod", mod_display)
            
            if stat == "DEX":
                self.set_value("Initiative", mod_display)

    def set_proficiencies(self):
        self.set_value("Proficiency Bonus", f"+{self.character.prof_bonus}")
        
        for check in self.character.checks:
            if check.is_proficient:
                self.set_value(f"{check.name} Checkbox", "Yes")
            
            self.set_value(check.name, str(check.score))

        self.set_value("Passive Perception", str(self.character.passive_perception))

    def set_spellcasting(self):
        spellcasting = self.character.spellcasting
    
        if spellcasting:
            self.set_value("Features and Traits", f"""\
Spell Save DC = {spellcasting.save_DC}
[8 + Prof Bonus + {spellcasting.base} Mod]

Spell Attack Mod = +{spellcasting.attack}
[Prof Bonus + {spellcasting.base} Mod]""")

    def set_miscellaneous(self):
        self.set_value("Class and Level", f" , Lv {self.character.level}")
        self.set_value("XP", str(self.character.xp))
        self.set_value("HP Max", self.character.hp)
        self.set_value("Hit Dice Total", str(self.character.level))
        self.set_value("Hit Dice", f"1d{self.character.hit_dice}")

    def set_value(self, key, value):
        self.output[self.fields[key]] = value
