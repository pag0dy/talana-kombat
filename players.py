# Clases base para crear jugadores

class Player:
    def __init__(self, n):
        ''' Función constructora de jugadores para participar en Talanakombat.
            :params n, string que indica el nombre del jugador
            :params attacks, diccionario que contiene las combinaciones de teclas que cada jugador utilizará para realizar un ataque, la cantidad de energía que este ataque le quita a su oponente, y el nombre de este ataque.
            :params energy, int que indica la energía que tiene el jugador al partir.
            :params direction, string que indica la dirección en la que ataca el jugador. 
        '''
        self.name = n
        self.attacks = {'combinations': [], 'damages': [], 'names':[]}
        self.energy = 6
        self.direction = ''


    def sayHi(self):
        ''' Función que presenta al jugador.
        '''
        print(f'Hola!, mi nombre es {self.name}.')


    def attack(self, combo_list):
        '''Función que procesa las combinaciones de teclas de cada jugador y devuelve el movimiento, golpe o ataque que estas representan.
            :params combo_list, tupla de movimientos y golpes que cada jugador ejecuta en un turno.
            :retorna damage, int que indica la energía que le quita a su oponente el ataque ejecutado.
        '''
        # Diccionario que permite identificar e interpretar movimientos que no son parte de un ataque.
        loose_moves = {'W': 'hacia arriba', 'S':'hacia abajo', 'A':'a la izquierda', 'D':'a la derecha'}
       # Diccionario que permite identificar e interpretar golpes que no son parte de una combinación de ataque.
        loose_attacks = {'P': 'puño', 'K':'patada'}
        combo_names = self.attacks['names']
        combo_damage = self.attacks['damages']
        if combo_list == '':
            damage = 0
        else:
        # Lista que combina la tupla de movimientos y golpes de cada turno
            combination = combo_list[0] + combo_list[1]
            this_move = f'{self.name}'
            damage = 0
            # Primero se intenta detectar una combinación de teclas que calce con uno de los ataques del jugador.
            if combination in self.attacks['combinations']:
                index = self.attacks['combinations'].index(combination)
                this_move += f' conecta un {combo_names[index]}'
                damage = combo_damage[index]
            # Si la combinación de teclas no es un ataque, se separa la primera tecla y se evalúa como un movimiento independiente.
            # Luego, se vuelve a evaluar si la combinación de teclas restante calza con un ataque del jugador. 
            else:
                i = 0
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
                        index = self.attacks['combinations'].index(char)
                        damage = combo_damage[index]
                    elif combination[i:len(combination)] in self.attacks['combinations']:
                        index = self.attacks['combinations'].index(combination)
                        this_move += f' conecta un {combo_names[index]}'    
                        damage = combo_damage[index] 
                    i += 1
            print(this_move)
        return damage
        


    def update_energy(self, damage):
        '''Función que actualiza la enegería del jugador después del turno del oponente.
            :params damage, int que representa el daño que le hace al jugador el ataque del oponente
            :retorna la energía actualizada del jugador.
            '''
        self.energy -= damage
        return self.energy


    def reset_energy(self):
        '''Función que devuelve la energía al jugador, para un nuevo combate.
            :retorna la energía actualizada del jugador.
            '''
        self.energy = 6 
        return self.energy