from src.main import add, sub 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    
def test_sub(a, b):
    return a - b