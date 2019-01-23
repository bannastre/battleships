import pytest
from lib.models import Board

def test_board():
  board = Board(6,9)
  assert board.width == 6
  assert board.height == 9

def test_populate_squares():
  board = Board(4,3)
  assert len(board.squares) == 3
  assert len(board.squares[0]) == 4

def test_is_square_full():
  board = Board(4,3)
  assert board.is_square_full(2,2) == False
