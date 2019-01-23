import pytest
from lib.models import Ship

ship_length = 3
ship = Ship(ship_length) 

def test_ship():
  assert ship.length == ship_length

