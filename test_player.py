import pytest
from lib.player import Player

player = Player(1)

def test_player_number():
  assert player.number == 1

def test_player_board():
  assert type(player.board).__name__ == 'Board'
  assert len(player.board.squares[0]) == 10

def test_player_ships():
  assert type(player.ships).__name__ == 'dict'
  assert len(player.ships) == 3