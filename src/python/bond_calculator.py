import numpy as np
from typing import Dict

def bond_price(face_value: float, coupon_rate: float, years_to_maturity: float, ytm: float, payments_per_year: int = 2) -> float:
    """
    Calculate the clean price of a bond.

    Parameters
    ----------
    face_value : float
        The par value of the bond.
    coupon_rate : float
        The annual coupon rate (e.g., 0.05 for 5%).
    years_to_maturity : float
        The number of years until maturity.
    ytm : float
        The yield to maturity (annualized).
    payments_per_year : int, optional
        The number of coupon payments per year (default is 2).

    Returns
    -------
    float
        The clean price of the bond.
    """
    periods = years_to_maturity * payments_per_year
    coupon_payment = (face_value * coupon_rate) / payments_per_year
    discount_rate_per_period = ytm / payments_per_year

    # Price from coupon payments (annuity)
    coupon_pv = coupon_payment * (1 - (1 + discount_rate_per_period)**-periods) / discount_rate_per_period

    # Price from face value (lump sum)
    face_value_pv = face_value / (1 + discount_rate_per_period)**periods

    return coupon_pv + face_value_pv

def accrued_interest(face_value: float, coupon_rate: float, settlement_date: np.datetime64, last_coupon_date: np.datetime64, day_count_convention: str = '30/360') -> float:
    """
    Calculates accrued interest.
    NOTE: This is a simplified example. A full implementation would handle various conventions.
    """
    if day_count_convention == '30/360':
        days_in_period = 180
        days_accrued = (settlement_date - last_coupon_date).astype('timedelta64[D]').astype(int) # Simplified
    else: # Actual/Actual
        # Placeholder for more complex logic
        days_accrued = (settlement_date - last_coupon_date).astype('timedelta64[D]').astype(int)
        days_in_period = 182.5 # Approximate

    interest = (days_accrued / days_in_period) * (face_value * coupon_rate / 2)
    return interest

def get_bond_details(ticker: str) -> Dict:
    """
    Placeholder to fetch bond details for a given ticker.
    """
    print(f"Fetching details for {ticker}...")
    # In a real app, this would query a database or external API
    return {
        "face_value": 1000,
        "coupon_rate": 0.0275,
        "years_to_maturity": 2.5,
        "ytm": 0.0415,
        "payments_per_year": 2
    }
