# test_cafe_logic.py

from cafe_logic import calculate_total_cost

def test_calculate_total_cost():
    subtotal, tax, total = calculate_total_cost(100, 150, 10)
    assert subtotal == 260
    assert tax == 13.0
    assert total == 273.0

def test_calculate_total_cost_zero():
    subtotal, tax, total = calculate_total_cost(0, 0, 0)
    assert subtotal == 0
    assert tax == 0
    assert total == 0
