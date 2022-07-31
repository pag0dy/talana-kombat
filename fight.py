

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

 
    def prepare_fight(self):
        #Decide quién va primero
        if len(self.pl1_moves['movimientos'][0] + self.pl1_moves['golpes'][0]) < len(self.pl2_moves['movimientos'][0] + self.pl2_moves['golpes'][0]):
            print('Comienza atacando el jugador 1')
            fighting_order = (self.pl1, self.pl2)
            fight_line_up = [list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes'])), list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))]
        else:
            print('Comienza el jugador 2') 
            fighting_order = (self.pl2, self.pl1) 
            fight_line_up = [[list(zip(self.pl2_moves['movimientos'], self.pl2_moves['golpes']))], [list(zip(self.pl1_moves['movimientos'], self.pl1_moves['golpes']))]]
        print('*******')
        return fighting_order, fight_line_up

    def fight(self, fighting_order, fight_line_up):
        print('Fight!')
        i = 0
        player1 = fighting_order[0]
        player2 = fighting_order[1]
        while i in range(0,4):
            move1 = fight_line_up[0][i]
            move2 = fight_line_up[1][i]
            player1.attack(move1)
            player2.attack(move2)
            i += 1
        

        # fight_narration = list(zip(fighting_order, fight_line_up))
        # print(fight_narration(fighting_order, fight_line_up))
        # return fight_narration
        
        



