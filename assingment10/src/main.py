'''
Created on Jan 4, 2018

@author: admin
'''
from ui.console import Console
from game.play import BattleShip

class Play_BattleShip:
    def run(self):
        console = Console(BattleShip())
        console.run_menu()
    
    
if __name__ == '__main__':
    game = Play_BattleShip()
    game.run()