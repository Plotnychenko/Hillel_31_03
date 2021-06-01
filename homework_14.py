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

    def health_up(self):
        if (self._max_health - self.health) >= 10:
            self.health += 10
        else:
            self.health += (self._max_health - self.health)

    def base_skill_up(self):
        if self.base_skill < self._max_skill:
            self.base_skill += 1


class Mage(Unit):
    def __init__(self, name, clan=None):
        super().__init__(name, clan)
        self.weapon = random.choice(["air", "fire", "water"])
        self.base_skill = self.intelligence


class Archer(Unit):
    def __init__(self, name, clan=None):
        super().__init__(name, clan)
        self.weapon = random.choice(["bow", "crossbow"])
        self.base_skill = self.dexterity


class Knight(Unit):
    def __init__(self, name, clan=None):
        super().__init__(name, clan)
        self.weapon = random.choice(["sword", "ax", "lance"])
        self.base_skill = self.strength