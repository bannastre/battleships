class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.squares = []
    self.populate_squares()

  def populate_squares(self):
    number_of_rows = 0
    while number_of_rows < (self.height):
      number_of_squares = 0
      row = []
      while number_of_squares < (self.width):
        row.extend([False])
        number_of_squares += 1
      self.squares.extend([row])          
      number_of_rows += 1
  
  def is_square_full(self, x, y):
    return self.squares[self.height-1][self.width-1]