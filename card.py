class Card:
    def __init__(self, character, value, strength, energy, jokenpo):
        self._character = character
        self._value = value
        self._strength = strength
        self._energy = energy
        self._jokenpo = jokenpo

    @property
    def character(self):
        return self._character

    @property
    def value(self):
        return self._value

    @property
    def strength(self):
        return self._strength

    @property
    def energy(self):
        return self._energy

    @property
    def jokenpo(self):
        return self._jokenpo

    def __str__(self):
        return f'Character: {self.character};\nValue: {self.value};' \
               f'\nStrength: {self.strength};\nEnergy: {self.energy};\nJokenpo: {self.jokenpo}\n'
