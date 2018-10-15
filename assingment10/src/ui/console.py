'''
Created on Jan 4, 2018

@author: admin
'''
from game.entities import Point

class Console:
    def __init__(self, game):
        self.__game = game
    
    def ui_place_user_battleship(self):
        letter = {'A' : 0 , 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
        print("Place your battleship")
        try:
            l = input("Give the x coordinate of the head of the battleship: ")
            y = int(input("Give the y coordinate of the head of the battleship: "))
            dir = input("Give the direction of the battleship: ")
            x = letter[l]
            p = Point(x, y - 1)
            error = self.__game.user_place_battleship(p, dir)
            
            if p.outside():
                print("The head of the battleship is outside of the board")
                return 1#EXIT_FAILURE
            if dir != 'up' and dir != 'down' and dir != 'left' and dir != "right":
                print("The direction must be up, down, left, or right")
                return 1#EXIT_FAILURE
            if error == 1:
                print("Cannot place a battleship there!")
                return error
            
            return 0 #EXIT_SUCCESS
        
        except ValueError:
            print("The y coordinate must be an iteger!")
            return 1 #EXIT_FAILURE
        except KeyError:
            print ("The x coordinate must be a capital letter from A to H!")
            return 1#EXIT_FAILURE
                     
    def ui_place_user_cruiser(self):
        print("Place your cruiser")
        letter = {'A' : 0 , 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
        try:
            l = input("Give the x coordinate of the head of the cruiser: ")
            y = int(input("Give the y coordinate of the head of the cruiser: "))
            dir = input("Give the direction of the cruiser:")
            x = letter[l]
            p = Point(x, y - 1)

            error = self.__game.user_place_cruiser(p, dir)
            if p.outside():
                print("The head of the battleship is outside of the board")
                return 1#EXIT_FAILURE
            if dir != 'up' and dir != 'down' and dir != 'left' and dir != "right":
                print("The direction must be up, down, left, or right")
                return 1#EXIT_FAILURE
            if error == 1:
                print("Cannot place a cruiser there!")
                return error
            
            return 0 #EXIT_SUCCESS
        
        except ValueError:
            print("The coordinates must be integers!")
            return 1 #EXIT_FAILURE
        except KeyError:
            print ("The x coordinate must be a capital letter from A to H!")
            return 1#EXIT_FAILURE
    
    def ui_place_user_destroyer(self):
        print("Place your destroyer")
        letter = {'A' : 0 , 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
        try:
            l = input("Give the x coordinate of the head of the destroyer: ")
            y = int(input("Give the y coordinate of the head of the destroyer: "))
            dir = input("Give the direction of the destroyer:")
            x = letter[l]
            p = Point(x, y - 1)
            error = self.__game.user_place_destroyer(p, dir)
            if p.outside():
                print("The head of the battleship is outside of the board")
                return 1#EXIT_FAILURE
            if dir != 'up' and dir != 'down' and dir != 'left' and dir != "right":
                print("The direction must be up, down, left, or right")
                return 1#EXIT_FAILURE
            if error == 1:
                print("Cannot place a destroyer there!")
                return error
            
            return 0 #EXIT_SUCCESS
        except ValueError:
            print("The coordinates must be integers!")
            return 1 #EXIT_FAILURE
        except KeyError:
            print ("The x coordinate must be a capital letter from A to H!")
            return 1#EXIT_FAILURE
      
    def ui_place_user_ships(self):
        
        while self.ui_place_user_battleship():
            continue
        
        self.ui_print_boards()
        
        while self.ui_place_user_cruiser():
            continue
        
        self.ui_print_boards()
        
        while self.ui_place_user_destroyer():
            continue
          
    def ui_print_boards(self):
        board = self.__game.get_player_board()
        help_board = self.__game.get_player_help_board()
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print("   Your Ships                   Your moves")
        print("   1 2 3 4 5 6 7 8              1 2 3 4 5 6 7 8")
        print('  ------------------           ------------------')
        for i in range(8):
            row = ""
            row  = row + letter[i] + ' |'
            for j in range(8):
                row = row + board[i][j] + " "
                
            row = row + "|         " + letter[i] + " |"
            for j in range(8):
                row = row + help_board[i][j] + ' '
                
            print(row + "|")
        
        print('  ------------------           ------------------')
    
    def ui_user_move(self):
        print("Make your move")
        letter = {'A' : 0 , 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
        try:
            l = input("Give the x coordinate: ")
            y = int(input("Give the y coordinate: "))
            if len(l) > 1:
                print("Invalid move! The x coordinate must be a capital letter from A to H!")
                return 1 #EXIT_FAILURE
            x = letter[l]
            p = Point(x, y - 1)
            ret = self.__game.user_makes_move(p)
            if ret == 1:
                print("Invalid move. The coordinates are out of range")
                return 1#EXIT_FAILURE
            print(ret)
            return 0 #EXIT_SUCCESS
        except ValueError:
            print("Invalid move! The y coordinate must be an integer")
            return 1 #EXIT_FAILURE
        except KeyError:
            print ("Invalid move! The x coordinate must be a capital letter from A to H!")
            return 1 #EXIT_FAILURE
        except IndexError:
            print ("Invalid move! The y coordinate must be a natural number from 1 to 8")
            return 1 #EXIT_FAILURE
            
        
    def ui_computer_move(self):
        ret = self.__game.computer_makes_inteligent_move()
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print("Computer moves:", letter[ret[0]], ret[1] + 1)
        message = ret[2]
        print(message)
    
    def run_menu(self):
        print("Welcome to my BattleShip game!")
        print("You can place 1 battleship (4 squares), 1 cruiser(3, squares) and a destroyer(2 squares) on an 8x8 board")
        print("As a legend, we have:")
        print("'~' = water, empty place")
        print("'O' = Miss")
        print("'X' = Hit")
        print("'H' = square part of a ship")
        print("Good luck! \n")
        print("Place your ships!")

        self.__game.set_up()
        self.ui_print_boards()
        self.ui_place_user_ships() # The user places their ships
        self.ui_print_boards()
        winner = "You"
        while True:
            # the user moves first
            self.ui_user_move()
            if self.__game.check_win() == True:
                break
            
            self.ui_computer_move()
            if self.__game.check_lose() == True:
                winner = "Computer"
                break
            
            self.ui_print_boards()
        self.ui_print_boards()
        
        if winner == "You":
            print("Congratulations! You won the game :)")
        else:
            print("Sorry, the computer won the game. Good luck next time :)")