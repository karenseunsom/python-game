class Weapons:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def use(self, enemy):
        enemy.health -= self.power
        return f'\n{self.name} did {self.power} damage to {enemy.name}'


