import pytest
from temperature import celsius_to_fahrenheit


def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


def test_negative_celsius():
    assert celsius_to_fahrenheit(-40) == -40


def test_normal_body_temperature():
    assert celsius_to_fahrenheit(37) == 98.6


def test_decimal_temperature():
    assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)


def test_positive_temperature():
    assert celsius_to_fahrenheit(25) == 77


def test_freezing_temperature():
    assert celsius_to_fahrenheit(-10) == 14


def test_result_is_number():
    result = celsius_to_fahrenheit(20)
    assert isinstance(result, float)