import pytest
from lib.ship import Ship

ship_length = 3
ship_direction = 'horizontal'

def test_ship():
  ship = Ship(ship_length, ship_direction) 
  assert ship.length == ship_length

def test_ship_direction():
  ship = Ship(ship_length, ship_direction) 
  assert ship.direction == ship_direction

def test_ship_take_hit():
  ship = Ship(ship_length, ship_direction)
  assert ship.length == 3
  ship.take_hit()
  assert ship.length == 2

def test_is_ship_sunk():
  ship = Ship(0, ship_direction)
  assert ship.is_sunk() == True
