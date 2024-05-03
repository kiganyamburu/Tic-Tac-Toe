import math
import random

class player:
    def __init__(self,letter):
        # letter is X or 0
        self. letter = letter
    
    
    # All players to get their next move given a game 
    def get_move(self, game):
        pass
    
    class RandomComputer(Player):
        def __init__(self, letter):
            super().__init__(letter)
            
        def get_move(self, game):
            square = random.choice(game.available_movies())
            
        
    class HumanPlayer(Player):
        def __init__(self, letter):
            super().__init__(letter)
            
            def get_move(self, game):
                valid_square = False
                val = None
                while not valid_square:
                    square = inpu(self.letter + '\'s turn. Input move (0-9):')
                    #We're are going to check that this is a correct value by trying to cast 
                    # It to integer and if its not then we say its invalid 
                    #if that spot is not available not the board, we also say its invalid 
                    try:
                        val = int(square)
                        if val not in game.available_move():
                            raise ValueError
                        valid_square = True
                    except ValueError:
                        print('invalid square. Try again.')
                        
                return val
                        
                
                            
                            
        
        
        