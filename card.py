class Card:
    def __init__(self, character, value, strength, energy, jokenpo):
        self.__character = character
        self.__value = value
        self.__strength = strength
        self.__energy = energy
        self.__jokenpo = jokenpo

    @property
    def character(self):
        return self.__character

    @property
    def value(self):
        return self.__value

    @property
    def strength(self):
        return self.__strength

    @property
    def energy(self):
        return self.__energy

    @property
    def jokenpo(self):
        return self.__jokenpo

    def __str__(self):
        return f'Character: {self.character};\nValue: {self.value};' \
               f'\nStrength: {self.strength};\nEnergy: {self.energy};\nJokenpo: {self.jokenpo}\n'
