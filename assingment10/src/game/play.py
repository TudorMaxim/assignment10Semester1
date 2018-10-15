'''
Created on Jan 4, 2018

@author: admin
'''
from copy import copy, deepcopy
import random
from game.entities import Point

class BattleShip:
    def __init__(self):
        self.__player_board = None
        self.__computer_board = None
        self.__player_help_board = None
        self.__computer_help_board = None

    def get_player_board(self):
        return self.__player_board

    def get_computer_board(self):
        return self.__computer_board

    def get_player_help_board(self):
        return self.__player_help_board

    def get_computer_help_board(self):
        return self.__computer_help_board

    def set_player_board(self, value):
        self.__player_board = value

    def set_computer_board(self, value):
        self.__computer_board = value

    def set_player_help_board(self, value):
        self.__player_help_board = value

    def set_computer_help_board(self, value):
        self.__computer_help_board = value

    def user_place_battleship(self, head, dir):
        if dir == "up":
            if head.get_x() > 2: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i - 1][j] == '~' and self.__player_board[i - 2][j] == '~' and self.__player_board[i - 3][j] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i - 1][j] = 'H'
                    self.__player_board[i - 2][j] = 'H'
                    self.__player_board[i - 3][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "down":
            if head.get_x() < 5: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i + 1][j] == '~' and self.__player_board[i + 2][j] == '~' and self.__player_board[i + 3][j] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i + 1][j] = 'H'
                    self.__player_board[i + 2][j] = 'H'
                    self.__player_board[i + 3][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "left":
            if head.get_y() > 2: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i][j - 1] == '~' and self.__player_board[i][j - 2] == '~' and self.__player_board[i][j - 3] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i][j - 1] = 'H'
                    self.__player_board[i][j - 2] = 'H'
                    self.__player_board[i][j - 3] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "right":
            if head.get_y() < 5: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i][j + 1] == '~' and self.__player_board[i][j + 2] == '~' and self.__player_board[i][j + 3] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i][j + 1] = 'H'
                    self.__player_board[i][j + 2] = 'H'
                    self.__player_board[i][j + 3] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        return 1 #EXIT_FAILURE
    
    def user_place_cruiser(self, head, dir):
        if dir == "up":
            if head.get_x() > 1: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i - 1][j] == '~' and self.__player_board[i - 2][j] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i - 1][j] = 'H'
                    self.__player_board[i - 2][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "down":
            if head.get_x() < 6: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i + 1][j] == '~' and self.__player_board[i + 2][j] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i + 1][j] = 'H'
                    self.__player_board[i + 2][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "left":
            if head.get_y() > 1: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i][j - 1] == '~' and self.__player_board[i][j - 2] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i][j - 1] = 'H'
                    self.__player_board[i][j - 2] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "right":
            if head.get_y() < 6: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i][j + 1] == '~' and self.__player_board[i][j + 2] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i][j + 1] = 'H'
                    self.__player_board[i][j + 2] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        return 1 #EXIT_FAILURE
    
    def user_place_destroyer(self, head, dir):
        if dir == "up":
            if head.get_x() > 0: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i - 1][j] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i - 1][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "down":
            if head.get_x() < 7: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i + 1][j] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i + 1][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "left":
            if head.get_y() > 0: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i][j - 1] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i][j - 1] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "right":
            if head.get_y() < 7: 
                i = head.get_x()
                j = head.get_y()
                if self.__player_board[i][j] == '~' and self.__player_board[i][j + 1] == '~':
                    self.__player_board[i][j] = 'H'
                    self.__player_board[i][j + 1] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        return 1 #EXIT_FAILURE
    
    def computer_place_battleship(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        directions = ["up", "down", "left", "right"]
        x = random.choice(numbers)
        y = random.choice(numbers)
        dir = random.choice(directions)
        head = Point(x, y)
        if dir == "up":
            if head.get_x() > 2: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i - 1][j] == '~' and self.__computer_board[i - 2][j] == '~' and self.__computer_board[i - 3][j] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i - 1][j] = 'H'
                    self.__computer_board[i - 2][j] = 'H'
                    self.__computer_board[i - 3][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "down":
            if head.get_x() < 5: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i + 1][j] == '~' and self.__computer_board[i + 2][j] == '~' and self.__computer_board[i + 3][j] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i + 1][j] = 'H'
                    self.__computer_board[i + 2][j] = 'H'
                    self.__computer_board[i + 3][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "left":
            if head.get_y() > 2: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i][j - 1] == '~' and self.__computer_board[i][j - 2] == '~' and self.__computer_board[i][j - 3] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i][j - 1] = 'H'
                    self.__computer_board[i][j - 2] = 'H'
                    self.__computer_board[i][j - 3] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "right":
            if head.get_y() < 5: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i][j + 1] == '~' and self.__computer_board[i][j + 2] == '~' and self.__computer_board[i][j + 3] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i][j + 1] = 'H'
                    self.__computer_board[i][j + 2] = 'H'
                    self.__computer_board[i][j + 3] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        return 1 #EXIT_FAILURE

    def computer_place_cruiser(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        directions = ["up", "down", "left", "right"]
        x = random.choice(numbers)
        y = random.choice(numbers)
        dir = random.choice(directions)
        head = Point(x, y)
        if dir == "up":
            if head.get_x() > 1: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i - 1][j] == '~' and self.__computer_board[i - 2][j] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i - 1][j] = 'H'
                    self.__computer_board[i - 2][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "down":
            if head.get_x() < 6: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i + 1][j] == '~' and self.__computer_board[i + 2][j] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i + 1][j] = 'H'
                    self.__computer_board[i + 2][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "left":
            if head.get_y() > 1: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i][j - 1] == '~' and self.__computer_board[i][j - 2] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i][j - 1] = 'H'
                    self.__computer_board[i][j - 2] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "right":
            if head.get_y() < 6: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i][j + 1] == '~' and self.__computer_board[i][j + 2] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i][j + 1] = 'H'
                    self.__computer_board[i][j + 2] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        return 1 #EXIT_FAILURE
    
    def computer_place_destroyer(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        directions = ["up", "down", "left", "right"]
        x = random.choice(numbers)
        y = random.choice(numbers)
        dir = random.choice(directions)
        head = Point(x, y)
        if dir == "up":
            if head.get_x() > 0: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i - 1][j] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i - 1][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "down":
            if head.get_x() < 7: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i + 1][j] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i + 1][j] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "left":
            if head.get_y() > 0: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i][j - 1] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i][j - 1] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        elif dir == "right":
            if head.get_y() < 7: 
                i = head.get_x()
                j = head.get_y()
                if self.__computer_board[i][j] == '~' and self.__computer_board[i][j + 1] == '~':
                    self.__computer_board[i][j] = 'H'
                    self.__computer_board[i][j + 1] = 'H'
                    return 0 #EXIT_SUCCESS
            return 1 #EXIT_FAILURE
        
        return 1 #EXIT_FAILURE
    
    def computer_place_ships(self):
        
        while self.computer_place_battleship():
            continue
        
        while self.computer_place_cruiser():
            continue
        
        while self.computer_place_destroyer():
            continue
        
    def check_win(self):
        for i in range(8):
            for j in range(8):
                if self.__computer_board[i][j] == 'H' and self.__player_help_board[i][j] != 'X':
                    return False
        return True
    
    def check_lose(self):
        for i in range(8):
            for j in range(8):
                if self.__player_board[i][j] == 'H' and self.__computer_help_board[i][j] != 'X':
                    return False
        return True
    
    def user_makes_move(self, point):
        if point.get_x() < 0 or point.get_x() > 7 or point.get_y() < 0 or point.get_y() > 7:
            return 1 #EXIT_FAILURE
        
        i = point.get_x()
        j = point.get_y()
        if self.__computer_board[i][j] == 'H':
            self.__player_help_board[i][j] = 'X'
            return "Hit!"
        else:
            self.__player_help_board[i][j] = 'O'
            return "Miss!"
        
    def computer_makes_move(self):    
        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        x = random.choice(numbers)
        y = random.choice(numbers)
        if self.__player_board[x][y] == 'H':
            self.__computer_help_board[x][y] = 'X'
            self.__player_board[x][y] = 'X'
            return (x, y, "Hit!")
        else:
            self.__computer_help_board[x][y] = 'O'
            self.__player_board[x][y] = 'O'
            return (x, y, "Miss!")
    
    def computer_makes_inteligent_move(self):
        #              
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for i in range (8):
            for j in range (8):
                if self.__computer_help_board[i][j] == 'X':
                    for it in range(4):
                        x = i + directions[it][0]
                        y = j + directions[it][1]
                        p = Point(x, y)
                        if p.outside() == False and self.__computer_help_board[x][y] == '~':
                            if self.__player_board[x][y] == 'H':
                                self.__computer_help_board[x][y] = 'X'
                                self.__player_board[x][y] = 'X'
                                return (x, y, "Hit!")
                            else:
                                self.__computer_help_board[x][y] = 'O'
                                self.__player_board = 'O'
                                return (x, y, "Miss!")
        
        return self.computer_makes_move()
                
    def set_up(self):
        board = []
        #set up blank 8x8 board
        for i in range(8):
            board_row = []
            for j in range (8):
                board_row.append("~")
            board.append(board_row)
            
        #set up user and computer boards
        self.__player_board = copy(deepcopy(board))
        self.__player_help_board = copy(deepcopy(board))
        self.__computer_board = copy(deepcopy(board))
        self.__computer_help_board = copy(deepcopy(board))
        
        self.computer_place_ships()
