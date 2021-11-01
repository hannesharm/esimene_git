import ylesanne
import random

def test_proov():
    assert ylesanne.proov(1, 1) == 2
    assert ylesanne.proov(3, 4) == 7

    for i in range(10):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        assert ylesanne.proov(a, b) == a + b


