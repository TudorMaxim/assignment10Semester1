'''
Created on Jan 4, 2018

@author: admin
'''

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def outside(self):
        if self.__x < 0 or self.__y < 0 or self.__x > 7 or self.__y > 7:
            return True
        return False
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class Ship:
    def __init__(self, type, ship):
        self.__type = type
        self.__points = ship
    
    def get_type(self):
        return self.__type

    def get_points(self):
        return self.__points
    
    def append(self, value):
        self.__points.append(value)

class Board:
    def __init__(self):
        self.__battleship = None
        self.__cruiser = None
        self.__destroyer = None
        self.__board = None # An 8x8 matrix
    
    def get_battleship(self):
        return self.__battleship

    def get_cruiser(self):
        return self.__cruiser

    def get_destroyer(self):
        return self.__destroyer
    
    def get_board(self):
        return self.__board
    