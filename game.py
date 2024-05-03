class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(90)]
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row)+'|')
            
    @staticmethod
    def print_board_nums():
        number_board =[[str(1) for i in range(j*3), (j+1)*3] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row)+'|')
    
    def available_move(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True 
        return False
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
        
        
    while game.empty_squares():
        if letter == '0':
            square = o_player.get_move(game)
    else:
        square = x_player.get_move(game)
        
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + 'makes a move to square {square}')
                game.print_board()
                print('') 
                
                
                
            if game.current_winner:
                if print_game: