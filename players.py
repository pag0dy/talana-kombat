# Clases base para crear jugadores

class Player:
    def __init__(self, n):
        self.name = n
        self.attacks = {'combinations': [], 'damages': [], 'names':[]}
        self.energy = 6

    def sayHi(self):
        print(f'Hola!, mi nombre es {self.name}.')

    def attack(self, combo_list):
        loose_moves = {'W': 'arriba', 'S':'abajo', 'A':'izquierda', 'D':'derecha'}
        loose_attacks = {'P': 'puño', 'K':'patada'}
        combo_names = self.attacks['names']
        
        for combo in combo_list:
            if combo in self.attacks['combinations']:
                index = self.attacks['combinations'].index(combo)

                print(f'{self.name} {combo_names[index]}')
            else:
                for char in combo:
                    if char in loose_moves:
                        print(f'se mueve {loose_moves[char]}')
                    if char in loose_attacks:
                        print(f'conecta un golpe de {loose_attacks[char]}')
                    else:
                        pass
