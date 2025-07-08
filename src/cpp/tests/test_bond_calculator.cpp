// Using Catch2 for testing
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "../include/bond_calculator.hpp"

TEST_CASE("Bond Price Calculations", "[bond_price]") {
    SECTION("Price at Par") {
        double price = calculate_bond_price_cpp(1000.0, 0.05, 10.0, 0.05, 2);
        REQUIRE(price == Approx(1000.0).epsilon(0.001));
    }
    SECTION("Price at Discount") {
        double price = calculate_bond_price_cpp(1000.0, 0.05, 10.0, 0.06, 2);
        REQUIRE(price == Approx(925.61).epsilon(0.001));
    }
    SECTION("Price at Premium") {
        double price = calculate_bond_price_cpp(1000.0, 0.05, 10.0, 0.04, 2);
        REQUIRE(price == Approx(1081.76).epsilon(0.001));
    }
}
