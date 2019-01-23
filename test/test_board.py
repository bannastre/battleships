import pytest
from lib.models import Board, Ship

board = Board(6, 9)

def test_board():
  assert type(board.squares).__name__ == 'list'

def test_board_dimensions():
  assert board.width == 6
  assert board.height == 9

def test_populate_squares():
  assert len(board.squares) == 9
  assert len(board.squares[0]) == 6

def test_is_square_full():
  assert board.is_square_full(2, 2) == False

def test_place_ship_in_a_single_square():
  ship = Ship(1)
  board.place_ship(ship, 2, 2)
  assert board.is_square_full(2, 2) == True

def test_place_a_ship_with_length():
  ship = Ship(3)
  board.place_ship(ship, 2, 2)

  assert board.is_square_full(1, 1) == False
  assert board.is_square_full(1, 2) == False
  assert board.is_square_full(1, 3) == False

  assert board.is_square_full(2, 1) == False
  assert board.is_square_full(2, 2) == True
  assert board.is_square_full(2, 3) == False
  
  assert board.is_square_full(3, 1) == False
  assert board.is_square_full(3, 2) == True
  assert board.is_square_full(3, 3) == False

  assert board.is_square_full(4, 1) == False
  assert board.is_square_full(4, 2) == True
  assert board.is_square_full(4, 3) == False
  
  assert board.is_square_full(5, 1) == False
  assert board.is_square_full(5, 2) == False
  assert board.is_square_full(5, 3) == False
