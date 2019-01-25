import pytest
from lib.player import Player

def test_player_number():
  player1 = Player(1)
  assert player1.number == 1

def test_player_board():
  player1 = Player(1)
  assert type(player1.board).__name__ == 'Board'
  assert len(player1.board.squares[0]) == 10

def test_player_ships():
  player1 = Player(1)
  assert type(player1.ships).__name__ == 'dict'
  assert len(player1.ships) == 3

def test_player_add_opponent():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  assert player1.opponents[0].number == 2

def test_player_get_opponent():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  type(player1.get_opponent(2)).__name__ == 'Player'

def test_player_incoming_hit():
  player1 = Player(1)
  player1.board.place_ship(player1.ships['ship1'], 2, 2)
  assert player1.incoming(2, 2) == { 'hit': True, 'sunk': False, 'winner': False }

def test_player_incoming_miss():
  player1 = Player(1)
  assert player1.incoming(2, 2) == { 'hit': False, 'sunk': False, 'winner': False }

def test_player_take_turn_hit():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  player2.board.place_ship(player2.ships['ship1'], 2, 2)
  assert player2.ships['ship1'].length == 2
  player1.take_turn(2, 2, 2)
  assert player2.ships['ship1'].length == 1

def test_player_take_turn_miss():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  player2.board.place_ship(player2.ships['ship1'], 2, 2)
  assert player2.ships['ship1'].length == 2
  player1.take_turn(2, 4, 2)
  assert player2.ships['ship1'].length == 2

def test_player_sink_an_opponent_ship():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  player2.board.place_ship(player2.ships['ship1'], 2, 2)
  assert player1.take_turn(2, 2, 2)['sunk'] == False
  assert player1.take_turn(2, 3, 2)['sunk'] == True

def test_player_is_alive():
  player1 = Player(1)
  assert player1.is_alive() == True

def test_player_have_i_won():
  player1 = Player(1)
  player2 = Player(2)
  player2.ships.pop('ship2')
  player2.ships.pop('ship3')
  player1.add_opponent(player2)
  player2.board.place_ship(player2.ships['ship1'], 2, 2)
  assert player1.take_turn(2, 2, 2)['winner'] == False
  assert player1.take_turn(2, 3, 2)['winner'] == True