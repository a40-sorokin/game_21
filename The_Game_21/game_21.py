#def main():

class TheGame( ):
    mv_player_count = 0
    ll_player = [] # список игроков
    def __init__(self, iv_player_count:int):
        self.mv_player_count = iv_player_count
        # создаем игроков
        for i in range( int(self.mv_player_count) ):
            new_player = Player ( self )
            self.ll_player.append( new_player )
            
        print("The Game instance is created")
        
        
class Player( ):
    mo_game = None
    def __init__(self, io_game: TheGame):
        self.mo_game = io_game
        
        
        
print("hello from The Game 21")
gv_player_count = input('Enter player count:  ')
print("число игроков :", gv_player_count)

go_game = TheGame (gv_player_count)


input()
