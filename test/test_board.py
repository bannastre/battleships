import pytest
from lib.board import Board
from lib.ship import Ship

board_height = 9
board_width = 6
board = Board(board_width, board_height)

def test_board():
  assert type(board.squares).__name__ == 'list'

def test_board_dimensions():
  assert board.width == board_width
  assert board.height == board_height

def test_populate_squares():
  assert len(board.squares) == board_height
  assert len(board.squares[0]) == board_width

def test_is_square_full():
  assert board.is_square_full(2, 2) == False

def test_place_a_ship_horizontally():
  board.print()
  ship = Ship(3, 'horizontal')
  board.place_ship(ship, 2, 2)
  board.print()
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

def test_cannot_place_a_ship_on_another_ship():
  ship = Ship(3, 'horizontal')
  with pytest.raises(Exception):
    board.place_ship(ship, 2, 2)

def test_reset_board():
  board.reset()
  assert board.is_square_full(2, 2) == False

def test_place_a_ship_vertically():
  ship = Ship(3, 'vertical')
  board.place_ship(ship, 2, 1)
  assert board.is_square_full(1, 1) == False
  assert board.is_square_full(1, 2) == False
  assert board.is_square_full(1, 3) == False
  assert board.is_square_full(2, 1) == True
  assert board.is_square_full(2, 2) == True
  assert board.is_square_full(2, 3) == True
  assert board.is_square_full(3, 1) == False
  assert board.is_square_full(3, 2) == False
  assert board.is_square_full(3, 3) == False
  assert board.is_square_full(4, 1) == False
  assert board.is_square_full(4, 2) == False
  assert board.is_square_full(4, 3) == False
  assert board.is_square_full(5, 1) == False
  assert board.is_square_full(5, 2) == False
  assert board.is_square_full(5, 3) == False  