from math_series.series import Fibonacci
import pytest

def test_Fibonacci_one():
    actual = Fibonacci(0)
    expected = 0
    assert actual == expected
    
def test_Fibonacci_one():
    actual = Fibonacci(1)
    expected = 1
    assert actual == expected
    
def test_Fibonacci_two():
    actual = Fibonacci(2)
    expected = 2
    assert actual == expected
    
@pytest.mark.skip("pending")   
def test_Fibonacci_three():
    actual = Fibonacci(3)
    expected = 6
    assert actual == expected
    
@pytest.mark.skip("pending")   
def test_Fibonacci_four():
    actual = Fibonacci(4)
    expected = 24
    assert actual == expected
