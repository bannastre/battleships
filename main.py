from lib.player import Player

player1 = Player(1)
player2 = Player(2)

player1.add_opponent(player2)
player2.add_opponent(player1)

current_player = player1

def switch_player():
  return player2 if current_player == player1 else player1

def place_ships():
  print("Player %s - Place your ships!" %(current_player.number))
  for ship in current_player.ships:
    print('This ship is %s squares long with orientation: %s' %(ship.length, ship.direction))
    ship_placed = False
    while not ship_placed:
      x = input("x co-ordinate: ")
      y = input("y co-ordinate: ")
      if input("Place ship at location %s, %s? (y/N): " %(x, y)) in ['y', 'Y']:
        ship_placed = current_player.board.place_ship(ship, int(x), int(y))
  current_player.board.print()

def play_a_turn():
  opponent = switch_player()
  print('Player %s: Prepare to fire on your Opponent!' %(current_player.number))
  x = input("Choose an x co-ordinate to fire at: ")
  y = input("Choose a y co-ordinate to fire at: ")
  result = current_player.take_turn(opponent.number, int(x), int(y))
  print('Hit!') if result.hit else print('Miss.')
  return result

# Player 1
place_ships() 
current_player = switch_player()
# Player 2
place_ships()
current_player = switch_player()

winner = False
while not winner: 
  result = play_a_turn()
  current_player = switch_player()
  if result['sunk'] == True:
    print('You Sunk a Ship! Your Opponent has %s Ships left' %(current_player.ships_alive()))
  winner = result['winner']

current_player = switch_player()
print('Congratulations, Player %s! You won BATTLESHIPS!' %(current_player.number))