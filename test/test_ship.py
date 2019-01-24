import pytest
from lib.ship import Ship

ship_length = 3
ship_direction = 'horizontal'
ship = Ship(ship_length, ship_direction) 

def test_ship():
  assert ship.length == ship_length

def test_ship_direction():
  assert ship.direction == ship_direction
