# https://github.com/moritaporretti/lab10-MP-AN.git
# Partner 1: Morita Porretti
# Partner 2: Alula Nahu

import math
import pytest
from calculator import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 3) == -3
    assert subtract(-3, -3) == 0

def test_multiply():
    assert mul(2, 3) == 6
    assert mul(-1, 3) == -3
    assert mul(0, 100) == 0

def test_divide():
    assert div(6, 2) == 3
    assert div(-9, 3) == -3
    assert round(div(1, 3), 4) == round(0.3333, 4)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        div(5, 0)

def test_logarithm():
    assert round(logarithm(10, 1000), 4) == 3
    assert round(logarithm(2, 8), 4) == 3
    assert round(logarithm(math.e, math.e**2), 4) == 2

def test_log_invalid_argument():
    with pytest.raises(ValueError):
        logarithm(1, 10)
    with pytest.raises(ValueError):
        logarithm(-2, 10)
    with pytest.raises(ValueError):
        logarithm(2, -10)

def test_hypotenuse():
    assert round(hypotenuse(3, 4), 4) == 5.0
    assert round(hypotenuse(5, 12), 4) == 13.0
    assert round(hypotenuse(8, 15), 4) == 17.0

def test_sqrt():
    assert square_root(25) == 5
    assert round(square_root(2), 4) == round(math.sqrt(2), 4)
    with pytest.raises(ValueError):
        square_root(-9)