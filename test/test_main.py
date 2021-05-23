import main


def test_addition():
    assert main.addition(3, 4) == 7
    assert main.addition(10, 40) == 50
    assert main.addition(39, 40) == 79
    assert main.addition(39, 41) == 80

def test_subtraction():
    assert main.subtraction(3, 4) == -1
    assert main.subtraction(35, 40) == -5
    assert main.subtraction(39, 4) == 35
    assert main.subtraction(390, 4) == 386

def test_multiplication():
    assert main.multiplication(3, 4) == 21
    assert main.multiplication(5, 4) == 20
    assert main.multiplication(40, 4) == 160
    assert main.multiplication(20, 40) == 800



