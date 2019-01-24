class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.squares = []
    self.populate_squares()

  def populate_squares(self):
    self.squares = [[False for row in range(self.width)] for i in range(self.height)]
    
  def reset(self):
    self.populate_squares()

  def print(self):
    print('---------BattleShips--------')
    for row in self.squares: print(row) 
    print('----------------------------')
  
  def is_square_full(self, w, h):
    return self.squares[h - 1][w - 1]

  def are_squares_full(self, ship, w, h):
    for i in range(ship.length):
      try: 
        if self.squares[h - 1][w - 1]: raise ValueError('Squares are not empty')
        if ship.direction == 'vertical':
          h += 1
        else: 
          w += 1
      except IndexError:
        raise ValueError('Ships must be constrained to the board')
      except:
        raise

  def place_ship(self, ship, w, h):
    self.are_squares_full(ship, w, h)
    for i in range(ship.length):
      try: 
        self.squares[h - 1][w - 1] = True
        if ship.direction == 'vertical':
          h += 1
        else: 
          w += 1
      except:
        raise
