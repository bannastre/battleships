import pytest
from lib.models import Board

def test_board_location():
  board = Board(6,9)
  assert board.height == 6
  assert board.width == 9