class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.squares = []
    self.populate_squares()

  def print(self):
    print('---------BattleShips--------')
    for row in self.squares: print(row) 
    print('----------------------------')
  
  def populate_squares(self):
    self.squares = [[False for row in range(self.width)] for i in range(self.height)]
    
  def reset(self):
    self.populate_squares()

  def is_square_full(self, x, y):
    return not not self.squares[y - 1][x - 1]

  def sink_square(self, x, y):
    self.squares[y - 1][x - 1] = False

  def are_squares_full(self, ship, x, y):
    for i in range(ship.length):
      try: 
        if type(self.squares[y - 1][x - 1]).__name__ == 'Ship': raise ValueError('Squares are not empty')
        if ship.direction == 'vertical':
          y += 1
        else: 
          x += 1
      except IndexError:
        raise ValueError('Ships must be constrained to the board')
      except:
        raise

  def place_ship(self, ship, x, y):
    self.are_squares_full(ship, x, y)
    for i in range(ship.length):
      self.squares[y - 1][x - 1] = ship
      if ship.direction == 'vertical':
        y += 1
      else: 
        x += 1
