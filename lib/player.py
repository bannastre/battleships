from .board import Board
from .ship import Ship

class Player:
  def __init__(self, number):
    self.number = number
    self.board = Board(10, 10)
    self.ships = [
      Ship(2, 'horizontal'),
      Ship(4, 'horizontal'),
      Ship(3, 'vertical'),
    ]
    self.opponents = []

  def add_opponent(self, opponent):
    self.opponents.append(opponent)

  def get_opponent(self, opponent_number):
    return list(filter(lambda oppo: oppo.number == opponent_number, self.opponents))[0]
  
  def ships_alive(self):
    floaty_ships = list(filter(lambda ship: ship.length > 0, self.ships))
    return len(floaty_ships)

  def incoming(self, x, y):
    square = self.board.is_square_full(x, y)
    is_ship = True if type(square).__name__ == 'Ship' else square
    is_sunk = False
    if is_ship:
      is_sunk = self.board.squares[y - 1][x - 1].take_hit()
      self.board.sink_square(x, y)
    return { 'hit': is_ship, 'sunk': is_sunk, 'winner': self.ships_alive() <= 0 }

  def take_turn(self, opponent_number, x, y):
    opponent = self.get_opponent(opponent_number)
    return opponent.incoming(x, y)
