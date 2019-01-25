class Ship:
  def __init__(self, length, direction):
    self.length = length
    self.direction = direction

  def is_sunk(self):
    return self.length <= 0
  
  def take_hit(self):
    self.length -= 1
    return self.is_sunk()