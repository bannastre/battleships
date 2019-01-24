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

def test_add_opponent():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  assert player1.opponents[0].number == 2

def test_incoming_miss():
  player1 = Player(1)
  assert player1.incoming(2, 2) == False

def test_incoming_hit():
  player1 = Player(1)
  player1.board.place_ship(player1.ships['ship1'], 2, 2)
  assert player1.incoming(2, 2) == True

def test_fire_miss():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  assert player1.fire(2, 2, 2) == False

def test_fire_hit():
  player1 = Player(1)
  player2 = Player(2)
  player1.add_opponent(player2)
  player2.board.place_ship(player2.ships['ship1'], 2, 2)
  assert player1.fire(2, 2, 2) == True