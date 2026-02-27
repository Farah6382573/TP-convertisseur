import pytest
from src.convertisseur import (
    celsius_vers_fahrenheit,
    fahrenheit_vers_celsius,
    celsius_vers_kelvin,
    kelvin_vers_celsius,
)


def test_0c_to_32f():
    assert celsius_vers_fahrenheit(0) == 32.0


def test_100c_to_212f():
    assert celsius_vers_fahrenheit(100) == 212.0


def test_273_15k_to_0c():
    assert kelvin_vers_celsius(273.15) == 0.0


def test_minus_273_15c_to_0k():
    assert pytest.approx(celsius_vers_kelvin(-273.15)) == 0.0


def test_negative_kelvin_exception():
    with pytest.raises(ValueError):
        kelvin_vers_celsius(-1)


def test_decimal_value():
    assert pytest.approx(celsius_vers_fahrenheit(36.6)) == 97.88