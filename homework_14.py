# Homewrok 14
# E. Plotnychenko

import random


class Unit:
    def __init__(self, name, clan=None):
        self.name = name
        self.clan = clan
        self._max_health = 100
        self.health = self._max_health
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 1
        self._max_skill = 10
        self._unit_type = ""

    def __str__(self):
        unit_info = f'"Class": {self._unit_type},\n' \
                    f'"Name": {self.name},\n"Clan": {self.clan},\n' \
                    f'"Weapon": {self.weapon},\n' \
                    f'"Health": {self.health},\n' \
                    f'"Skills": "Intelligence": {self.intelligence}, "Strength": {self.strength}, "Dexterity": {self.dexterity}'
        return unit_info

    def health_up(self):
        if (self._max_health - self.health) >= 10:
            self.health += 10
        else:
            self.health += (self._max_health - self.health)

    def base_skill_up(self):
        if self._unit_type == "Mage" and self.intelligence < self._max_skill:
            self.intelligence += 1
        elif self._unit_type == "Archer" and self.dexterity < self._max_skill:
            self.dexterity += 1
        elif self._unit_type == "Knight" and self.strength < self._max_skill:
            self.strength += 1


class Mage(Unit):
    def __init__(self, name, clan=None):
        super().__init__(name, clan)
        self.weapon = random.choice(["air", "fire", "water"])
        self.unit_type = __class__.__name__

    def __str__(self):
        return super().__str__()


class Archer(Unit):
    def __init__(self, name, clan=None):
        super().__init__(name, clan)
        self.weapon = random.choice(["bow", "crossbow"])
        self.unit_type = __class__.__name__

    def __str__(self):
        return super().__str__()


class Knight(Unit):
    def __init__(self, name, clan=None):
        super().__init__(name, clan)
        self.weapon = random.choice(["sword", "ax", "lance"])
        self.unit_type = __class__.__name__

    def __str__(self):
        return super().__str__()
