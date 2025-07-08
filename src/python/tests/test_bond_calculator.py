import pytest
from src.python.bond_calculator import bond_price

def test_bond_price_at_par():
    """Test bond price when YTM equals the coupon rate."""
    price = bond_price(face_value=1000, coupon_rate=0.05, years_to_maturity=10, ytm=0.05, payments_per_year=2)
    assert abs(price - 1000.00) < 0.01

def test_bond_price_discount():
    """Test bond price when YTM is greater than the coupon rate."""
    price = bond_price(face_value=1000, coupon_rate=0.05, years_to_maturity=10, ytm=0.06, payments_per_year=2)
    assert abs(price - 925.61) < 0.01

def test_bond_price_premium():
    """Test bond price when YTM is less than the coupon rate."""
    price = bond_price(face_value=1000, coupon_rate=0.05, years_to_maturity=10, ytm=0.04, payments_per_year=2)
    assert abs(price - 1081.76) < 0.01 # Updated value from a standard calculator

def test_zero_coupon_bond():
    """Test price of a zero-coupon bond."""
    price = bond_price(face_value=1000, coupon_rate=0.0, years_to_maturity=5, ytm=0.03, payments_per_year=1)
    assert abs(price - 862.61) < 0.01
