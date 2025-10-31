import pytest
from hex import to_decimal, from_decimal

def test_to_decimal_basic():
    assert to_decimal("A", 16) == 10
    assert to_decimal("10", 2) == 2
    assert to_decimal("C7", 16) == 199
    assert to_decimal("Z", 36) == 35

def test_from_decimal_basic():
    assert from_decimal(10, 16) == "A"
    assert from_decimal(2, 2) == "10"
    assert from_decimal(199, 16) == "C7"
    assert from_decimal(35, 36) == "Z"

def test_round_trip():
    for base in range(2, 37):
        for num in [0, 1, 7, 15, 42, 1234]:
            s = from_decimal(num, base)
            assert to_decimal(s, base) == num

def test_invalid_input():
    with pytest.raises(ValueError):
        to_decimal("G", 16)
