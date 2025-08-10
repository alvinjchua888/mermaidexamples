import builtins
from subtract import subtract_two_numbers
import pytest

def test_subtract_two_numbers_positive(monkeypatch, capsys):
    # Simulate user input: 10 and 4.5
    inputs = iter(['10', '4.5'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    result = subtract_two_numbers()
    captured = capsys.readouterr()
    assert "The result of 10.0 - 4.5 is 5.5" in captured.out
    assert result == 5.5

def test_subtract_two_numbers_negative(monkeypatch, capsys):
    # Simulate user input: -2 and -5
    inputs = iter(['-2', '-5'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    result = subtract_two_numbers()
    captured = capsys.readouterr()
    assert "The result of -2.0 - -5.0 is 3.0" in captured.out
    assert result == 3.0

def test_subtract_two_numbers_zero(monkeypatch, capsys):
    # Simulate user input: 0 and 0
    inputs = iter(['0', '0'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    result = subtract_two_numbers()
    captured = capsys.readouterr()
    assert "The result of 0.0 - 0.0 is 0.0" in captured.out
    assert result == 0.0

def test_subtract_two_numbers_invalid_input(monkeypatch, capsys):
    # Simulate user input: 'abc' and '5'
    inputs = iter(['abc', '5'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    result = subtract_two_numbers()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numeric values." in captured.out
    assert result is None