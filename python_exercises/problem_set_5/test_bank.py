from bank import value

def test_assert():
    assert value("hello") == 0
    assert value("How are you?") == 20
    assert value("Sorry") == 100
