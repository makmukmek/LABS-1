from distance import calculate
from circle import *
from operations import calc_nums
from favorite_movies import sort_mov
from my_family import height
from zoo import zoo_shaffles
from secret import decoder
#import pytest

#Тест для distance
def test_calculate_distances():
    sites = {
    'Seattle' : (150, 500),
    'Washington' : (500, 150),
    'Los-Angeles' : (350,350)
    }
    expected_dist = {'Seattle': {'Seattle': 0.0, 'Washington': 494.9747468305833, 'Los-Angeles': 250.0},
                'Washington': {'Seattle': 494.9747468305833, 'Washington': 0.0, 'Los-Angeles': 250.0},
                'Los-Angeles': {'Seattle': 250.0, 'Washington': 250.0, 'Los-Angeles': 0.0}}
    actual_dist = calculate(sites)
    assert expected_dist == actual_dist

#Тест для circle
def test_calc_circle():
    assert calc_circle(12) == 452.3893
    assert calc_circle(23) == 1661.9025
    assert calc_circle(34) == 3631.6810
def test_is_in():
    assert is_in((1, 2), 5) == True
    assert is_in((2, 3), 8) == True
    assert is_in((3, 4), 3) == False
    assert is_in((4, 5), 2) == False

#Тест для operations
def test_calc_nums():
    assert calc_nums() == 25

#Тест для favorite_movies
def test_sort_mov():
    assert sort_mov() == ' '

#Тест для my_family
def test_height():
    assert height() == ' '

#Тест для zoo
def test_zoo_shaffles():
    assert zoo_shaffles() == ' '

#Тест для secret
def test_decoder():
    assert decoder() == "в бане веник дороже денег"
