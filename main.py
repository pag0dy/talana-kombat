from players import Player
from fight import Fight
import time
import sys
import json

def iniciar_talanakombat():
    time.sleep(1)
    print('Bienvenidos a...')
    time.sleep(1)
    print('--------------------------------------------------')
    print('▀█▀ ▄▀█ █░░ ▄▀█ █▄░█ ▄▀█ █▄▀ █▀█ █▀▄▀█ █▄▄ ▄▀█ ▀█▀')
    print('░█░ █▀█ █▄▄ █▀█ █░▀█ █▀█ █░█ █▄█ █░▀░█ █▄█ █▀█ ░█░')
    print('--------------------------------------------------')
    choice = input('Por favor, ingresa 0 si quieres partir con peleas de prueba, o 1 si quieres ingresar tu propia pelea. \n Si quieres salir, ingresa Q:')
    if choice == '0':
        # Inicia la primera pelea de prueba
        fight_1 = Fight(player1, player2, {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}})
        fight_sequence = fight_1.prepare_fight()
        fight_1.fight(fight_sequence[0], fight_sequence[1])
        # Inicia la segunda pelea de prueba
        fight_2 = Fight(player1, player2, {"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"], "golpes":["K", "P", "K", "P"]}, "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}})
        fight_sequence_2 = fight_2.prepare_fight()
        fight_2.fight(fight_sequence_2[0], fight_sequence_2[1])
        # Inicia la tercera pelea de prueba
        fight_3 = Fight(player1, player2,{"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}})
        fight_sequence_3 = fight_3.prepare_fight()
        fight_3.fight(fight_sequence_3[0], fight_sequence_3[1])
        iniciar_talanakombat()
    elif choice == '1':
        pelea_ingresada = input('Por favor pega el JSON con los movimientos de la pelea:')
        pelea = json.loads(pelea_ingresada)
        try:
            created_fight = Fight(player1, player2, dict(pelea))
            fight_sequence_4 = created_fight.prepare_fight()
            created_fight.fight(fight_sequence_4[0], fight_sequence_4[1])
        except Exception:
            print(sys.exc_info())
            print('Ups! algo falló!')
        iniciar_talanakombat()
    elif choice.upper() == 'Q':
        print('Adios!')
        quit()
    else:
        print('Lo siento, no reconozco ese comando. Intenta de nuevo.')
        iniciar_talanakombat()
# Crear jugadores con sus atributos
if __name__ == "__main__":
    player1 = Player('Tonyn Stallone')        
    player1.attacks['combinations'] =  ['DSDP', 'SDK', 'P', 'K']
    player1.attacks['damages'] = [3, 2, 1, 1]
    player1.attacks['names'] = ['Taladoken', 'Remuyuken', 'Puño', 'Patada']
    player1.direction = 'D'

    player2 = Player('Arnaldor Shuatseneguer')
    player2.attacks['combinations'] = ['SAK', 'ASAP', 'P', 'K'] 
    player2.attacks['damages'] = [3, 2, 1, 1]  
    player2.attacks['names'] = ['Remuyuken','Taladoken','Puño', 'Patada']
    player2.direction = 'A'   
    iniciar_talanakombat()
    


        