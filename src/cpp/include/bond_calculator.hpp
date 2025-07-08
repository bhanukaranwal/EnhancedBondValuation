#include "bond_calculator.hpp"
#include <cmath>

/**
 * @brief High-performance calculation of a bond's clean price.
 *
 * This function uses a direct formula for performance.
 *
 * @param face_value The par value of the bond.
 * @param coupon_rate The annual coupon rate (e.g., 0.05 for 5%).
 * @param years_to_maturity Years until the bond matures.
 * @param ytm Annual yield to maturity.
 * @param payments_per_year Number of coupon payments per year.
 * @return double The clean price of the bond.
 */
double calculate_bond_price_cpp(double face_value, double coupon_rate, double years_to_maturity, double ytm, int payments_per_year) {
    double periods = years_to_maturity * payments_per_year;
    double coupon_payment = (face_value * coupon_rate) / payments_per_year;
    double discount_rate = ytm / payments_per_year;

    if (discount_rate == 0) { // Avoid division by zero
        return face_value + (coupon_payment * periods);
    }

    double coupon_pv = coupon_payment * (1.0 - std::pow(1.0 + discount_rate, -periods)) / discount_rate;
    double face_value_pv = face_value / std::pow(1.0 + discount_rate, periods);

    return coupon_pv + face_value_pv;
}
