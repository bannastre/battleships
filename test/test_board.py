import pytest
from lib.models import Board

board = Board(6, 9)

def test_board():
  assert board.width == 6
  assert board.height == 9

def test_populate_squares():
  assert len(board.squares) == 9
  assert len(board.squares[0]) == 6

def test_is_square_full():
  assert board.is_square_full(2, 2) == False

def test_place_ship_in_a_single_square():
  board.place_ship(2, 2)
  assert board.is_square_full(2, 2) == True
