import pytest
from lib.board import Board
from lib.ship import Ship

board_width = 6
board_height = 9

def test_board():
  board = Board(board_width, board_height)
  assert type(board.squares).__name__ == 'list'

def test_board_dimensions():
  board = Board(board_width, board_height)
  assert board.width == board_width
  assert board.height == board_height

def test_populate_squares():
  board = Board(board_width, board_height)
  assert len(board.squares) == board_height
  assert len(board.squares[0]) == board_width

def test_is_square_full():
  board = Board(board_width, board_height)
  assert board.is_square_full(2, 2) == False

def test_place_a_ship_horizontally():
  board = Board(board_width, board_height)
  ship = Ship(3, 'horizontal')
  board.place_ship(ship, 2, 2)
  board.print()
  assert board.squares[0] == [False, False, False, False, False, False]
  assert board.squares[1] == [False, ship, ship, ship, False, False]
  assert board.squares[2] == [False, False, False, False, False, False]

def test_cannot_place_a_ship_on_another_ship():
  board = Board(board_width, board_height)
  ship = Ship(3, 'horizontal')
  board.place_ship(ship, 2, 2)
  with pytest.raises(Exception):
    board.place_ship(ship, 2, 2)

def test_reset_board():
  board = Board(board_width, board_height)
  ship = Ship(3, 'horizontal')
  board.place_ship(ship, 2, 2)
  board.reset()
  assert board.is_square_full(2, 2) == False

def test_place_a_ship_vertically():
  board = Board(board_width, board_height)
  ship = Ship(3, 'vertical')
  board.place_ship(ship, 2, 2)
  board.print()
  assert board.squares[0] == [False, False, False, False, False, False]
  assert board.squares[1] == [False, ship, False, False, False, False]
  assert board.squares[2] == [False, ship, False, False, False, False]
  assert board.squares[3] == [False, ship, False, False, False, False]
  assert board.squares[4] == [False, False, False, False, False, False]

def test_ships_are_constrained_to_the_board():
  board = Board(board_width, board_height)
  horizontal_ship = Ship(3, 'horizontal')
  vertical_ship = Ship(3, 'vertical')
  with pytest.raises(Exception):
    board.place_ship(horizontal_ship, 5, 2)
  with pytest.raises(Exception):
    board.place_ship(vertical_ship, 5, 9)

def test_sink_square():
  board = Board(board_width, board_height)
  ship = Ship(3, 'horizontal')
  board.place_ship(ship, 2, 2)
  assert board.squares[1] == [False, ship, ship, ship, False, False]
  board.sink_square(2, 2) 
  assert board.squares[1] == [False, 'Sunk', ship, ship, False, False]