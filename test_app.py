# test_app.py
from app import soma, eh_par

def test_soma():
    assert soma(2, 3) == 5

def test_eh_par():
    assert eh_par(4) is True
    assert eh_par(7) is False