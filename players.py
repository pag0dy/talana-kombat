# Clases base para crear jugadores

class Player:
    def __init__(self, n):
        self.name = n
        self.attacks = {'combinations': [], 'damages': [], 'names':[]}
        self.energy = 6
        self.direction = ''

    def sayHi(self):
        print(f'Hola!, mi nombre es {self.name}.')

    def attack(self, combo_list):
        loose_moves = {'W': 'hacia arriba', 'S':'hacia abajo', 'A':'a la izquierda', 'D':'a la derecha'}
        loose_attacks = {'P': 'puño', 'K':'patada'}
        combo_names = self.attacks['names']
        combination = combo_list[0] + combo_list[1]
        i = 0
        this_move = f'{self.name}'
        if combination in self.attacks['combinations']:
            index = self.attacks['combinations'].index(combination)
            this_move += f' conecta un {combo_names[index]}'
        else:
            while i in range(0, len(combination)):                       
                char = list(combination).pop(i)
                if char in loose_moves:
                    if len(this_move) > len(f'{self.name}'):
                        this_move += f', luego {loose_moves[char]}'
                    else:
                        this_move += f' se mueve {loose_moves[char]}'
                elif char in loose_attacks:
                    if len(this_move) > len(f'{self.name}'):
                        this_move += f' y conecta un golpe de {loose_attacks[char]}'
                    else:
                        this_move += f' conecta un golpe de {loose_attacks[char]}'
                elif combination[i:len(combination)] in self.attacks['combinations']:
                    index = self.attacks['combinations'].index(combination)
                    this_move += f' conecta un {combo_names[index]}'      
                i += 1
        print(this_move)
