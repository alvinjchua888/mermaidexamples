import builtins
from add import add_two_numbers
import pytest

def test_add_two_numbers(monkeypatch, capsys):
    # Simulate user input: 3 and 4.5
    inputs = iter(['3', '4.5'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    add_two_numbers()
    captured = capsys.readouterr()
    assert "The sum is:" in captured.out
    assert "7.5" in captured.out

def test_add_two_numbers_negative(monkeypatch, capsys):
    # Simulate user input: -2 and -5
    inputs = iter(['-2', '-5'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    add_two_numbers()
    captured = capsys.readouterr()
    assert "The sum is:" in captured.out
    assert "-7.0" in captured.out

def test_add_two_numbers_zero(monkeypatch, capsys):
    # Simulate user input: 0 and 0
    inputs = iter(['0', '0'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    add_two_numbers()
    captured = capsys.readouterr()
    assert "The sum is:" in captured.out
    assert "0.0" in captured.out