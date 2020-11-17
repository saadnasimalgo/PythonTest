from .python_test import copy_command, open_file, parse_command, functional_command

import pytest


def test_opening_file():
    assert open_file()


def test_raises_exception_on_not_opening():
    with pytest.raises(FileNotFoundError):
        print(f'No file found')


def test_copy_command():
    assert copy_command()


def test_raises_exception_on_copy_command():
    with pytest.raises(AssertionError):
        print(f'No copy data found')


def test_parse_command():
    assert parse_command()


def test_raises_exception_on_parse_command():
    with pytest.raises(AssertionError):
        print(f'No parse data found')


def functional_commands():
    assert functional_command()


def test_raises_exception_on_functional_commands():
    with pytest.raises(AssertionError):
        print(f'No functional data found')