import pytest
from greetbot import greet


def test_greet_normal():
    assert greet("Alice") == "Hello, Alice! GreetBot welcomes you."


def test_greet_empty_string():
    assert greet("") == "Hello, ! GreetBot welcomes you."


def test_greet_with_numbers():
    assert greet("R2D2") == "Hello, R2D2! GreetBot welcomes you."
