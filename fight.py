

# Clase de pelea
class Fight:
    def __init__(self, player1, player2, pelea):
        self.pl1_moves = pelea["player1"]
        self.pl2_moves = pelea["player2"]
        self.pl1 = player1
        self.pl2 = player2

    def resumen_pelea(self):
        print(f'El jugador 1 tiene los siguientes movimientos: {self.pl1_moves}')
        print(f'El jugador 2 tiene los siguientes movimientos: {self.pl2_moves}')

 
    def start_fight(self):
        if len(self.pl1_moves['movimientos'][0] + self.pl1_moves['golpes'][0]) < len(self.pl2_moves['movimientos'][0] + self.pl2_moves['golpes'][0]):
            print('Comienza atacando el jugador 1')
            # fight_line_up = {[self.pl1_moves, self.pl1],[self.pl2_moves, self.pl2]}
            fight_line_up = [[self.pl1, list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes']))], [self.pl2, list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))]]
        else:
            print('Comienza el jugador 2')  
            fight_line_up = [[self.pl2, list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))], [self.pl1, list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes']))]]
        print(fight_line_up)
        combinations = lambda x,y: x+y
        combo_list = []
        for i in fight_line_up[0][1]:
            combo_list.append(combinations(i[0], i[1]))
        print(combo_list)
        fight_line_up[0][0].attack(combo_list)

        # print(list(zip(fight_line_up[1]['movimientos'], fight_line_up[1]['golpes'])))

