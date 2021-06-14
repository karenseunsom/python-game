class Character:
    def __init__(self, name, health=100, power=5):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other_person):
        other_person.health -= self.power
        print(f'\n{self.name} does {self.power} damage to {other_person.name}')
        
    def is_alive(self):
        self.health > 0

    # def print_status(self):
    #     return f'{self.name} has {self.health} and {self.power}.'

    def __str__(self):
        return f'{self.name} has {self.health} HP and {self.power} power.'

    
