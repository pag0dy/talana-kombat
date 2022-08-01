import time
# Clase de pelea

class Fight:
    def __init__(self, player1, player2, pelea):
        '''Función constructora de la clase Peleas.
           :params player1 y player2, los jugadores que participarán en este combate (instancias de la clase Player).
           :params pelea, JSON con los movimientos y golpes de cada jugador.
        '''
        self.pl1_moves = pelea["player1"]
        self.pl2_moves = pelea["player2"]
        self.pl1 = player1
        self.pl2 = player2
        self.counter = 0

    def prepare_fight(self):
        '''Función que decide quién parte atacando y retorna los parámetros necesarios para comenzar la pelea.
            :retorna fighting_order, lista con los jugadores en el órden en el que atacarán.
            :retorna fighting_line_up, lista con los movimientos y golpes de cada jugador, en el mismo órden de la lista anterior.
            '''
        # Se evalúa si esta es la primera pelea entre los jugadores o si es un desempate.
        if self.counter == 0:
            if len(self.pl1_moves['movimientos'][0] + self.pl1_moves['golpes'][0]) < len(self.pl2_moves['movimientos'][0] + self.pl2_moves['golpes'][0]):
                time.sleep(1)
                print('------------------------------')
                print('Comienza atacando el jugador 1')
                print('------------------------------')
                fighting_order = (self.pl1, self.pl2)
                fight_line_up = [list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes'])), list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))]
            else:
                time.sleep(1)
                print('------------------------------')
                print('Comienza atacando el jugador 2') 
                print('------------------------------')
                fighting_order = (self.pl2, self.pl1) 
                fight_line_up = [list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes'])), list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes']))]

        elif self.counter == 1:
            if len(self.pl1_moves['movimientos'][0]) < len(self.pl2_moves['movimientos'][0]):
                time.sleep(1)
                print('------------------------------')
                print('Comienza atacando el jugador 1')
                print('------------------------------')
                fighting_order = (self.pl1, self.pl2)
                fight_line_up = [list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes'])), list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))]
            else:
                time.sleep(1)
                print('------------------------------')
                print('Comienza atacando el jugador 2') 
                print('------------------------------')
                fighting_order = (self.pl2, self.pl1) 
                fight_line_up = [list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes'])), list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes']))]

        elif self.counter == 2:
            if len(self.pl1_moves['golpes'][0]) < len(self.pl2_moves['golpes'][0]):
                time.sleep(1)
                print('------------------------------')
                print('Comienza atacando el jugador 1')
                print('------------------------------')
                fighting_order = (self.pl1, self.pl2)
                fight_line_up = [list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes'])), list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))]
            else:
                time.sleep(1)
                print('------------------------------')
                print('Comienza atacando el jugador 2') 
                print('------------------------------')
                fighting_order = (self.pl2, self.pl1) 
                fight_line_up = [list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes'])), list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes']))]

        else:
            time.sleep(1)
            print('------------------------------')
            print('Comienza atacando el jugador 1')
            print('------------------------------')
            fighting_order = (self.pl1, self.pl2)
            fight_line_up = [list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes'])), list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))]

        return fighting_order, fight_line_up
        
    def fight(self, fighting_order, fight_line_up):
        ''' Función que ejecuta la pelea y muestra el resultado de esta.
            :params fighting_order, tupla que entrega los jugadores en el órden en el que van a combatir.
            :params fight_line_up, lista que combina los movimientos y golpes de cada jugador en el órden correspondiente.
        '''
        time.sleep(1)
        print('-----------------------')
        print('█▀█ █▀▀ ▄▀█ █▀▄ █▄█ ▀█ ▀█')
        print('█▀▄ ██▄ █▀█ █▄▀ ░█░ ░▄ ░▄')
        print('-----------------------')
        time.sleep(1)
        print('-----------------------')
        print('█▀▀ █ █▀▀ █░█ ▀█▀ █ █ █')
        print('█▀░ █ █▄█ █▀█ ░█░ ▄ ▄ ▄')
        print('-----------------------')
        # Se asignan los jugadores según el órden en el que atacarán
        player1 = fighting_order[0]
        player2 = fighting_order[1]
        # Se aseegura de que ambos jugadores comiencen con la energía completa
        player1.reset_energy()
        player2.reset_energy()
        i = 0
        fight_turns = len(fight_line_up[0]) if len(fight_line_up[0]) > len(fight_line_up[1]) else len(fight_line_up[1])
        while i in range(0,fight_turns):
            if i < len(fight_line_up[0]):
                move1 = fight_line_up[0][i]
            else:
                move1 = ''
            if i < len(fight_line_up[1]):
                move2 = fight_line_up[1][i]
            else:
                move2 = ''
            time.sleep(1)
            damage1 = player1.attack(move1)
            player2.update_energy(damage1)  
            time.sleep(1)
            damage2 = player2.attack(move2)
            player1.update_energy(damage2)
            if player1.energy <= 0 and player2.energy > 0:
                time.sleep(1)
                print(f'{player2.name} es el ganador!')
                time.sleep(1)
                print('*********************************************************')
                print('█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀   █▀▀ █░█ ▄▀█ █▀▄▀█ █▀█ █')
                print('█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ ▄█   █▄▄ █▀█ █▀█ █░▀░█ █▀▀ ▄')
                print('*********************************************************')
                time.sleep(2)
                break
            elif player2.energy <= 0 and player1.energy > 0:
                time.sleep(1)
                print(f'{player1.name} es el ganador!')
                print('*********************************************************')
                print('█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀   █▀▀ █░█ ▄▀█ █▀▄▀█ █▀█ █')
                print('█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ ▄█   █▄▄ █▀█ █▀█ █░▀░█ █▀▀ ▄')
                print('*********************************************************')
                time.sleep(2)
                break
            elif player2.energy <= 0 and player1.energy <= 0:
                time.sleep(1)
                print(f'Empate! Se viene un nuevo combate!')
                print('******************************')
                print('█▀▀ █▀█   ▄▀█ █▀▀ ▄▀█ █ █▄░█ █')
                print('█▄█ █▄█   █▀█ █▄█ █▀█ █ █░▀█ ▄')
                print('******************************')
                time.sleep(2)
                self.counter += 1
                break
            i += 1
        
        
        



