from players import Player
from fight import Fight


# Crear jugadores con sus atributos

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


fight_1 = Fight(player1, player2, {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}})
fight_sequence = fight_1.prepare_fight()
fight_1.fight(fight_sequence[0], fight_sequence[1])

fight_2 = Fight(player1, player2, {"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"], "golpes":["K", "P", "K", "P"]}, "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}})
fight_sequence_2 = fight_2.prepare_fight()
fight_2.fight(fight_sequence_2[0], fight_sequence_2[1])