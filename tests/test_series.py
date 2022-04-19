from math_series.series import ft
import pytest

def test_ft_one():
    actual = ft(1)
    expected = 1
    assert actual == expected
