# Clases base para crear jugadores

class Player:
    def __init__(self, n):
        self.name = n
        self.attack_1 = ''
        self.attack_2 = ''
        self.attack_3 = ''
        self.attack_4 = ''
        self.damage_1 = 0
        self.damage_2 = 0
        self.damage_3 = 0
        self.damage_4 = 0
        self.combination_1 = ''
        self.combination_2 = ''
        self.combination_3 = ''
        self.combination_4 = ''
        self.energy = 6

    def sayHi(self):
        print(f'Hola!, mi nombre es {self.name}.')
    

# Crear jugadores con sus atributos

player1 = Player('Tonyn Stallone')        
player1.attack_1 = 'Taladoken'
player1.damage_1 = 3
player1.combination_1 = 'DSDP'
player1.attack_2 = 'Remuyuken'
player1.damage_2 = 2
player1.combination_2 = 'SDK'
player1.attack_3 = 'Puño'
player1.damage_3 = 1
player1.combination_3 = 'P'
player1.attack_4 = 'Patada'
player1.damage_4 = 1
player1.combination_4 = 'K'
player1.sayHi()

player2 = Player('Arnaldor Shuatseneguer')        
player2.attack_1 = 'Remuyuken'
player2.damage_1 = 3
player2.combination_1 = 'SAK'
player2.attack_2 = 'Taladoken'
player2.damage_2 = 2
player2.combination_2 = 'ASAP'
player2.attack_3 = 'Puño'
player2.damage_3 = 1
player2.combination_3 = 'P'
player2.attack_4 = 'Patada'
player2.damage_4 = 1
player2.combination_4 = 'K'
player2.sayHi()