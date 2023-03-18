class Card:
    def __init__(self, character, value, strength, energy, jokenpo):
        self.character = character
        self.value = value
        self.strength = strength
        self.energy = energy
        self.jokenpo = jokenpo

    def __str__(self):
        print(f'Character: {self.character};\nValue: {self.value};'
              f'\nStrength: {self.strength};\nEnergy: {self.energy};\nJokenpo: {self.jokenpo}\n')

