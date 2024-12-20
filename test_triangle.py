import right_triangle_area as rta   # Make sure you can access the code you want to test
def test_simple_triangle():
    assert rta.right_triangle_area(3, 4) == 6.0      # PASS

def test_null_triangle():
    assert rta.right_triangle_area(0, 0) == 0.0      # PASS

def test_incorrect_triangle():
    assert rta.right_triangle_area(-1, -1) == 0.0    # FAIL