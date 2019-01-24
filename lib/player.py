from .board import Board
from .ship import Ship

class Player:
  def __init__(self, number):
    self.number = number
    self.board = Board(10, 10)
    self.ships = {
      'ship1': Ship(2, 'horizontal'),
      'ship2': Ship(4, 'horizontal'),
      'ship3': Ship(3, 'vertical'),
    }
