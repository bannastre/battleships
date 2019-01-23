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
  
  def is_square_full(self, x, y):
    return self.squares[self.height-1][self.width-1]