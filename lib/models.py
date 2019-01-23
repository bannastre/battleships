class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.squares = []
    self.populate_squares()

  def populate_squares(self):
    while len(self.squares) < (self.height):
      row = [False] * self.width
      self.squares.extend([row]) 
  
  def is_square_full(self, w, h):
    return self.squares[h - 1][w - 1]
  
  def place_ship(self, ship, w, h):
    number_of_squares = 0
    while number_of_squares < ship.length:
      self.squares[h - 1][w - 1] = True
      w += 1
      number_of_squares += 1

class Ship:
  def __init__(self, length):
    self.length = length