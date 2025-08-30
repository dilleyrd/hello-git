import math
from temp_utils import c_to_f, f_to_c

def test_freezing_point():
    assert math.isclose(c_to_f(0.0), 32.0, rel_tol=0.0, abs_tol=1e-9)
    assert math.isclose(f_to_c(32.0), 0.0, rel_tol=0.0, abs_tol=1e-9)

def test_boiling_point():
    assert math.isclose(c_to_f(100.0), 212.0, rel_tol=0.0, abs_tol=1e-9)
    assert math.isclose(f_to_c(212.0), 100.0, rel_tol=0.0, abs_tol=1e-9)
