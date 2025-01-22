import pytest
from maximizingElementInArray import maxElement

def test_maxElement():
    assert maxElement(4, 6, 1) == 2
    assert maxElement(6, 10, 3) == 3
    assert maxElement(5, 15, 2) == 4
    assert maxElement(3, 3, 0) == 1
    assert maxElement(1, 100, 0) == 100

def test_maxElement_edge_cases():
    assert maxElement(1, 1, 0) == 1
    assert maxElement(2, 1, 0) == 1
    assert maxElement(2, 3, 1) == 2
    assert maxElement(3, 6, 1) == 3
    assert maxElement(3, 6, 2) == 2

if __name__ == "__main__":
    pytest.main()