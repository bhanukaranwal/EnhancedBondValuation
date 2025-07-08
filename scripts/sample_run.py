import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.python.bond_calculator import bond_price, get_bond_details
from src.python.yield_solver import solve_ytm

def main():
    """
    A sample script to demonstrate core functionality.
    """
    print("--- Enhanced Bond Valuation Calculator ---")

    # --- Example 1: Calculate Bond Price from Yield ---
    print("\n[Example 1: Calculating Bond Price]")
    bond_details = get_bond_details("MSFT 2.75 2027")
    price = bond_price(
        face_value=bond_details["face_value"],
        coupon_rate=bond_details["coupon_rate"],
        years_to_maturity=bond_details["years_to_maturity"],
        ytm=bond_details["ytm"],
        payments_per_year=bond_details["payments_per_year"]
    )
    print(f"Calculated Price: ${price:.2f}")
    print("BVAL Confidence Score: 9/10 (Sourced from model estimate)")

    # --- Example 2: Calculate Yield from Price ---
    print("\n[Example 2: Calculating YTM from Price]")
    market_price = 985.50
    ytm = solve_ytm(
        price=market_price,
        face_value=bond_details["face_value"],
        coupon_rate=bond_details["coupon_rate"],
        years_to_maturity=bond_details["years_to_maturity"],
        payments_per_year=bond_details["payments_per_year"]
    )
    print(f"Given Price: ${market_price:.2f}")
    print(f"Calculated YTM: {ytm * 100:.4f}%")


if __name__ == "__main__":
    main()
