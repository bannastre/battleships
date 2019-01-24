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
    self.opponents = []

  def add_opponent(self, opponent):
    self.opponents.append(opponent)

  def fire(self, opponent_number, x, y):
    for oppo in self.opponents:
      if oppo.number == opponent_number:
        return oppo.incoming(x, y)

  def incoming(self, x, y):
    is_hit = self.board.is_square_full(x, y)
    if is_hit:
      self.board.sink_square(x, y)
    return is_hit

      