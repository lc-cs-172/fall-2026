"""Unit tests for linear search."""

__author__ = 'Alain Kägi'

import activities.search.linear as linear

def test_empty():
    assert linear.search([], 0) == -1

def test_singleton():
    a = [0]
    assert linear.search(a, 0) == 0
    assert linear.search(a, 1) == -1

def test_five():
    a = [0, 1, 2, 3, 4, 5]
    assert linear.search(a, 0) == 0
    assert linear.search(a, 1) == 1
    assert linear.search(a, 2) == 2
    assert linear.search(a, 3) == 3
    assert linear.search(a, 4) == 4
    assert linear.search(a, 5) == 5
    assert linear.search(a, 6) == -1

def test_strings():
    a = ['ant', 'ape', 'bee', 'cat', 'dog', 'eel', 'elkcow', 'gnu', 'owl', 'pig', 'rat', 'yak']
    assert linear.search(a, 'bee') == 2
    assert linear.search(a, 'zebra') == -1
