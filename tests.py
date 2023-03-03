import pytest
from parce import get_args_dict


def test_pos():
    def f(x, y, z):
        return 0
    assert get_args_dict(f, args=[1, 2, 3], kwargs={}) == {'x': 1, 'y': 2, 'z': 3}


def test_named():
    def f(x, y, z):
        return 0
    assert get_args_dict(f, args=[], kwargs={'x': 1, 'y': 2, 'z': 3}) == {'x': 1, 'y': 2, 'z': 3}


def test_named_and_pos():
    def f(x, y, z):
        return 0
    assert get_args_dict(f, args=[1, 2], kwargs={'z': 3}) == {'x': 1, 'y': 2, 'z': 3}


def test_defaults_and_pos():
    def f(x, y, z=3):
        return 0
    assert get_args_dict(f, args=[1, 2], kwargs={}) == {'x': 1, 'y': 2, 'z': 3}


def test_defaults_and_named():
    def f(x, y, z=3):
        return 0
    assert get_args_dict(f, args=[], kwargs={'x': 1, 'y': 2}) == {'x': 1, 'y': 2, 'z': 3}


def test_defaults_and_mixed():
    def f(x, y, z=3):
        return 0
    assert get_args_dict(f, args=[1], kwargs={'y': 2}) == {'x': 1, 'y': 2, 'z': 3}


def test_defaults_changed_named():
    def f(x, y=2, z=2):
        return 0
    assert get_args_dict(f, args=[1], kwargs={'z': 3}) == {'x': 1, 'y': 2, 'z': 3}


def test_defaults_changed_pos():
    def f(x, y=3, z=2):
        return 0
    assert get_args_dict(f, args=[1, 2, 3], kwargs={}) == {'x': 1, 'y': 2, 'z': 3}


def test_args_unpacking():
    def f(x, y, z, *args):
        return 0
    assert get_args_dict(f, args=[1, 2, 3, 4, 5, 6], kwargs={}) == {'x': 1, 'y': 2, 'z': 3, 'args': [4, 5, 6]}


def test_kwargs_unpacking():
    def f(x, y, z, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2, 3], kwargs={'a': 10}) == {'x': 1, 'y': 2, 'z': 3, 'kwargs': {'a': 10}, 'a': 10}


def test_named_and_kwargs_unpacking():
    def f(x, y, z, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2], kwargs={'z': 3, 'a': 10}) == {'x': 1, 'y': 2, 'z': 3, 'kwargs': {'a': 10},
                                                                       'a': 10}


def test_defaults_with_args():
    def f(x, y, *args, z=3):
        return 0
    assert get_args_dict(f, args=[1, 2, 5, 6], kwargs={}) == {'x': 1, 'y': 2, 'z': 3, 'args': [5, 6]}


def test_defaults_changes_with_args():
    def f(x, y, *args, z=5):
        return 0
    assert get_args_dict(f, args=[1, 2, 5, 6], kwargs={'z': 3}) == {'x': 1, 'y': 2, 'z': 3, 'args': [5, 6]}


def test_defaults_with_kwargs():
    def f(x, y, z=3, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2], kwargs={'a': 10}) == {'x': 1, 'y': 2, 'z': 3, 'kwargs': {'a': 10}, 'a': 10}


def test_defaults_change_with_kwargs():
    def f(x, y, z=5, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2, 3], kwargs={'a': 10}) == {'x': 1, 'y': 2, 'z': 3, 'kwargs': {'a': 10}, 'a': 10}


def test_args_with_kwargs():
    def f(x, y, *args, z=3, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2, 5, 6], kwargs={'a': 10}) == {'x': 1, 'y': 2, 'z': 3, 'args': [5, 6],
                                                                     'kwargs': {'a': 10}, 'a': 10}


def test_named_with_args():
    def f(x, y, z, *args):
        return 0
    assert get_args_dict(f, args=[1, 2], kwargs={'z': 3}) == {'x': 1, 'y': 2, 'z': 3, 'args': []}


def test_kwarg_in_kwarg():
    def f(x, y, z, *args, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2], kwargs={'z': 3, 'args': 10, 'kwargs': 100}) == {
        'x': 1, 'y': 2, 'z': 3, 'args': [], 'kwargs': {'args': 10, 'kwargs': 100}}


def test_kwarg_in_kwarg2():
    def f(x, y, z, *args, **kwargs):
        return 0
    assert get_args_dict(f, args=[1, 2, 3, 4, 5], kwargs={'args': 10, 'kwargs': 100}) == {
        'x': 1, 'y': 2, 'z': 3, 'args': [4, 5], 'kwargs': {'args': 10, 'kwargs': 100}}


def test_lambda():
    assert get_args_dict(lambda x, y, z: 0, args=[1, 2, 3], kwargs={}) == {'x': 1, 'y': 2, 'z': 3}
