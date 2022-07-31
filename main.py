from players import Player
from fight import Fight


# Crear jugadores con sus atributos

player1 = Player('Tonyn Stallone')        
player1.attacks['combinations'] =  ['DSDP', 'SDK', 'P', 'K']
player1.attacks['damages'] = [3, 2, 1, 1]
player1.attacks['names'] = ['Taladoken', 'Remuyuken', 'Puño', 'Patada']

player2 = Player('Arnaldor Shuatseneguer')
player2.attacks['combinations'] = ['SAK', 'ASAP', 'P', 'K'] 
player2.attacks['damages'] = [3, 2, 1, 1]     

fight_1 = Fight(player1, player2, {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}})
fight_1.start_fight()